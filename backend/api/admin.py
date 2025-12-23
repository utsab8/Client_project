from django.contrib import admin, messages
from django.utils.html import mark_safe
from .models import Product, Category, Tag, Order, SiteSettings
from .utils import send_payment_verified_email


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
    list_display = ['name', 'original_price', 'price', 'discount_percentage', 'is_active', 'is_featured', 'created_at']
    list_filter = ['is_active', 'is_featured', 'category', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ['tags']
    readonly_fields = ['price', 'created_at', 'updated_at']
    
    class Media:
        js = ('api/js/product_price_calculator.js',)
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Add help text to make it clear
        if 'original_price' in form.base_fields:
            form.base_fields['original_price'].help_text = 'Original price before discount (e.g., ₹299)'
        if 'discount_percentage' in form.base_fields:
            form.base_fields['discount_percentage'].help_text = 'Enter discount percentage (e.g., 33 for 33% off). Price will be calculated automatically.'
        if 'price' in form.base_fields:
            form.base_fields['price'].help_text = 'Automatically calculated: Original Price - (Original Price × Discount %). This is what customers pay.'
        return form
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'description', 'short_description')
        }),
        ('Pricing', {
            'fields': ('original_price', 'discount_percentage', 'price'),
            'description': 'Set Original Price and Discount Percentage. The discounted price will be calculated automatically.'
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
    list_display = ['id', 'customer_name', 'email', 'product', 'total_amount', 'status', 'created_at', 'payment_screenshot_thumb']
    list_filter = ['status', 'created_at', 'bump_offer_added']
    search_fields = ['email', 'phone', 'customer_name', 'payment_id']
    readonly_fields = ['created_at', 'updated_at', 'payment_screenshot_preview']
    actions = ['mark_payment_verified']
    
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
            'fields': ('status', 'payment_id', 'payment_screenshot', 'payment_screenshot_preview', 'download_link', 'download_sent')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def payment_screenshot_preview(self, obj):
        if obj.payment_screenshot and hasattr(obj.payment_screenshot, 'url'):
            url = obj.payment_screenshot.url
            return mark_safe(
                f'<a href="{url}" target="_blank" rel="noopener">'
                f'<img src="{url}" style="max-height:200px; border-radius:8px;" />'
                f'</a>'
            )
        return "No screenshot uploaded"
    payment_screenshot_preview.short_description = "Payment Screenshot Preview"

    def payment_screenshot_thumb(self, obj):
        if obj.payment_screenshot and hasattr(obj.payment_screenshot, 'url'):
            url = obj.payment_screenshot.url
            return mark_safe(
                f'<a href="{url}" target="_blank" rel="noopener">'
                f'<img src="{url}" style="height:40px; border-radius:4px;" />'
                f'</a>'
            )
        return "-"
    payment_screenshot_thumb.short_description = "Screenshot"

    def mark_payment_verified(self, request, queryset):
        updated = 0
        for order in queryset:
            order.status = 'verified'
            order.save(update_fields=['status', 'updated_at'])
            try:
                send_payment_verified_email(order)
            except Exception as exc:
                print(f"Failed to send verified email for order {order.id}: {exc}")
            updated += 1
        self.message_user(request, f"{updated} order(s) marked as verified and email sent.", messages.SUCCESS)
    mark_payment_verified.short_description = "Mark payment as verified (send email)"


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('General', {
            'fields': ('site_name', 'site_tagline', 'payment_qr_default')
        }),
        ('Contact & Social', {
            'fields': ('whatsapp_number', 'instagram_url', 'youtube_url', 'support_email', 'from_email')
        }),
        ('Footer & SEO', {
            'fields': ('footer_links', 'meta_description')
        }),
        ('Policies', {
            'fields': ('privacy_policy', 'terms_and_conditions', 'refund_policy')
        }),
    )

    def has_add_permission(self, request):
        # Only allow one settings object
        return not SiteSettings.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False


