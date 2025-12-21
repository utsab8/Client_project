from rest_framework import serializers
from .models import Product, Category, Tag, Order, SiteSettings


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description']


class ProductListSerializer(serializers.ModelSerializer):
    """Serializer for product list view (minimal data)"""
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    display_image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'short_description', 'price', 'original_price',
            'discount_percentage', 'display_image', 'badge_text', 'category', 'tags',
            'is_featured', 'created_at'
        ]

    def get_display_image(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return obj.image_url or ''


class ProductDetailSerializer(serializers.ModelSerializer):
    """Serializer for product detail view (full data)"""
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    display_image = serializers.SerializerMethodField()
    related_products = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'description', 'short_description',
            'price', 'original_price', 'discount_percentage', 'display_image',
            'badge_text', 'features', 'what_included', 'perfect_for',
            'category', 'tags', 'is_featured', 'created_at', 'updated_at',
            'related_products'
        ]

    def get_display_image(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return obj.image_url or ''

    def get_related_products(self, obj):
        """Get related products (same category or tags)"""
        related = Product.objects.filter(is_active=True).exclude(id=obj.id)
        
        # Filter by category first
        if obj.category:
            related = related.filter(category=obj.category)
        
        # If not enough, add by tags
        if related.count() < 5 and obj.tags.exists():
            tag_related = Product.objects.filter(
                is_active=True,
                tags__in=obj.tags.all()
            ).exclude(id=obj.id).distinct()
            related = (related | tag_related).distinct()
        
        serializer = ProductListSerializer(related[:5], many=True, context=self.context)
        return serializer.data


class OrderCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating orders"""
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_slug = serializers.CharField(source='product.slug', read_only=True)

    class Meta:
        model = Order
        fields = [
            'id', 'email', 'phone', 'customer_name', 'product', 'product_name',
            'product_slug', 'quantity', 'unit_price', 'total_amount',
            'bump_offer_added', 'bump_offer_price', 'status', 'payment_id',
            'created_at'
        ]
        read_only_fields = ['unit_price', 'total_amount', 'status', 'payment_id']

    def create(self, validated_data):
        product = validated_data['product']
        validated_data['unit_price'] = product.price
        
        # Calculate total
        quantity = validated_data.get('quantity', 1)
        total = product.price * quantity
        
        if validated_data.get('bump_offer_added') and validated_data.get('bump_offer_price'):
            total += validated_data['bump_offer_price']
        
        validated_data['total_amount'] = total
        return super().create(validated_data)


class OrderDetailSerializer(serializers.ModelSerializer):
    """Serializer for order details"""
    product = ProductListSerializer(read_only=True)

    class Meta:
        model = Order
        fields = [
            'id', 'email', 'phone', 'customer_name', 'product', 'quantity',
            'unit_price', 'total_amount', 'discount_amount', 'bump_offer_added',
            'bump_offer_price', 'status', 'payment_id', 'download_link',
            'download_sent', 'created_at', 'updated_at'
        ]


class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = '__all__'


