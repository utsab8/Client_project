from django.contrib import admin
from .models import Product, Category, Tag, Order, SiteSettings


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'original_price', 'discount_percentage', 'is_active', 'is_featured', 'created_at']
    list_filter = ['is_active', 'is_featured', 'category', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ['tags']
    readonly_fields = ['discount_percentage', 'created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'description', 'short_description')
        }),
        ('Pricing', {
            'fields': ('price', 'original_price', 'discount_percentage')
        }),
        ('Media', {
            'fields': ('image', 'image_url')
        }),
        ('Categorization', {
            'fields': ('category', 'tags', 'badge_text')
        }),
        ('Product Details', {
            'fields': ('features', 'what_included', 'perfect_for')
        }),
        ('Status', {
            'fields': ('is_active', 'is_featured')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'email', 'product', 'total_amount', 'status', 'created_at']
    list_filter = ['status', 'created_at', 'bump_offer_added']
    search_fields = ['email', 'phone', 'customer_name', 'payment_id']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Customer Information', {
            'fields': ('email', 'phone', 'customer_name')
        }),
        ('Order Details', {
            'fields': ('product', 'quantity', 'unit_price', 'total_amount', 'discount_amount')
        }),
        ('Bump Offer', {
            'fields': ('bump_offer_added', 'bump_offer_price')
        }),
        ('Payment & Status', {
            'fields': ('status', 'payment_id', 'download_link', 'download_sent')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Only allow one settings object
        return not SiteSettings.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False


