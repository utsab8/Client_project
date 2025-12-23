from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from .models import Product, Category, Tag, Order, SiteSettings
from .serializers import (
    ProductListSerializer, ProductDetailSerializer,
    CategorySerializer, TagSerializer,
    OrderCreateSerializer, OrderDetailSerializer,
    SiteSettingsSerializer
)
from .utils import send_order_confirmation_email, send_download_link_email


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for viewing products.
    Provides list and detail views.
    """
    queryset = Product.objects.filter(is_active=True)
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'tags', 'is_featured']
    search_fields = ['name', 'description', 'short_description']
    ordering_fields = ['created_at', 'price', 'name']
    ordering = ['-created_at']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductDetailSerializer
        return ProductListSerializer

    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Get featured products"""
        products = self.queryset.filter(is_featured=True)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_price(self, request):
        """Filter products by price range"""
        min_price = request.query_params.get('min_price')
        max_price = request.query_params.get('max_price')
        
        queryset = self.queryset
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_category(self, request):
        """Get products by category slug"""
        category_slug = request.query_params.get('category')
        if category_slug:
            queryset = self.queryset.filter(category__slug=category_slug)
        else:
            queryset = self.queryset
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for viewing categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'

    @action(detail=True, methods=['get'])
    def products(self, request, slug=None):
        """Get all products in a category"""
        category = self.get_object()
        products = Product.objects.filter(category=category, is_active=True)
        serializer = ProductListSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for viewing tags.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'

    @action(detail=True, methods=['get'])
    def products(self, request, slug=None):
        """Get all products with a tag"""
        tag = self.get_object()
        products = Product.objects.filter(tags=tag, is_active=True)
        serializer = ProductListSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)


class OrderViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing orders.
    """
    queryset = Order.objects.all()
    permission_classes = [AllowAny]  # Change to IsAuthenticated in production

    def get_serializer_class(self):
        if self.action == 'create':
            return OrderCreateSerializer
        return OrderDetailSerializer

    def create(self, request, *args, **kwargs):
        """Create a new order"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        
        # Send order confirmation email
        try:
            send_order_confirmation_email(order)
        except Exception as e:
            # Log error but don't fail the order creation
            print(f"Failed to send order confirmation email: {e}")
        
        # If order has download link and is completed, send download link email
        if order.download_link and order.status == 'completed':
            try:
                send_download_link_email(order)
            except Exception as e:
                print(f"Failed to send download link email: {e}")
        
        # Return order details
        detail_serializer = OrderDetailSerializer(order, context={'request': request})
        return Response(detail_serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['patch'])
    def update_status(self, request, pk=None):
        """Update order status (for payment gateway callbacks)"""
        order = self.get_object()
        new_status = request.data.get('status')
        payment_id = request.data.get('payment_id')
        download_link = request.data.get('download_link')
        
        old_status = order.status
        old_download_link = order.download_link
        
        if new_status:
            order.status = new_status
        if payment_id:
            order.payment_id = payment_id
        if download_link:
            order.download_link = download_link
        
        order.save()
        
        # Send download link email if download link was added and order is completed
        if download_link and order.status == 'completed' and not old_download_link:
            try:
                send_download_link_email(order)
            except Exception as e:
                print(f"Failed to send download link email: {e}")
        
        # Send confirmation email if status changed to completed
        if new_status == 'completed' and old_status != 'completed':
            try:
                send_order_confirmation_email(order)
            except Exception as e:
                print(f"Failed to send order confirmation email: {e}")
        
        serializer = OrderDetailSerializer(order, context={'request': request})
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_email(self, request):
        """Get orders by email"""
        email = request.query_params.get('email')
        if not email:
            return Response({'error': 'Email parameter required'}, status=status.HTTP_400_BAD_REQUEST)
        
        orders = self.queryset.filter(email=email)
        serializer = OrderDetailSerializer(orders, many=True, context={'request': request})
        return Response(serializer.data)


class SiteSettingsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for site settings.
    """
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        """Always return the first (and only) settings object"""
        obj, created = SiteSettings.objects.get_or_create(pk=1)
        return obj


