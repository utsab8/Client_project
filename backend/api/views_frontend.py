from django.shortcuts import render, get_object_or_404
from django.http import Http404

from api.models import Product, Category, Tag

def index(request):
    """Homepage view - Fully dynamic"""
    # Get price filter from URL
    price_filter = request.GET.get('price')
    
    # Get all active products
    products = Product.objects.filter(is_active=True).order_by('-created_at')
    
    # Filter by price if specified
    if price_filter:
        try:
            price_value = float(price_filter)
            products = products.filter(price=price_value)
        except ValueError:
            # Invalid price filter, ignore it
            pass
    
    context = {
        'products': products,
        'price_filter': price_filter,
    }
    
    return render(request, 'index.html', context)

def product(request):
    """Product detail page view - Fully dynamic"""
    # Get product slug from URL parameter
    product_slug = request.GET.get('slug') or request.GET.get('product')
    
    if not product_slug:
        # If no slug provided, redirect to homepage or show error
        from django.shortcuts import redirect
        return redirect('index')
    
    # Get product from database
    try:
        product_obj = get_object_or_404(Product, slug=product_slug, is_active=True)
    except Http404:
        # Product not found
        return render(request, 'product.html', {
            'error': 'Product not found',
            'product': None
        })
    
    # Get related products (same category or tags)
    # Start with base queryset
    base_queryset = Product.objects.filter(is_active=True).exclude(id=product_obj.id)
    
    # Filter by category first
    if product_obj.category:
        related_products = base_queryset.filter(category=product_obj.category)
    else:
        related_products = base_queryset.none()  # Empty queryset if no category
    
    # If not enough, add by tags
    if product_obj.tags.exists():
        tag_related = base_queryset.filter(
            tags__in=product_obj.tags.all()
        ).distinct()
        
        # Combine querysets properly
        if related_products.exists():
            # Use union to combine querysets
            related_products = related_products.union(tag_related)
        else:
            related_products = tag_related
    
    # Limit to 5 related products and ensure distinct
    related_products = related_products.distinct()[:5]
    
    # Prepare context
    context = {
        'product': product_obj,
        'related_products': related_products,
        'category': product_obj.category,
        'tags': product_obj.tags.all(),
    }
    
    return render(request, 'product.html', context)

def checkout(request):
    """Checkout page view - Fully dynamic"""
    # Get product slug from URL parameter
    product_slug = request.GET.get('slug') or request.GET.get('product')
    
    if not product_slug:
        # If no slug provided, redirect to homepage
        from django.shortcuts import redirect
        return redirect('index')
    
    # Get product from database
    try:
        product_obj = get_object_or_404(Product, slug=product_slug, is_active=True)
    except Http404:
        # Product not found
        return render(request, 'checkout.html', {
            'error': 'Product not found',
            'product': None
        })
    
    context = {
        'product': product_obj,
    }
    
    return render(request, 'checkout.html', context)


