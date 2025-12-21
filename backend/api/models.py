from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator


class Category(models.Model):
    """Product Category Model"""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Tag(models.Model):
    """Product Tag Model"""
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    """Product Model"""
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField()
    short_description = models.TextField(max_length=500, blank=True)
    
    # Pricing
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    original_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(0)])
    discount_percentage = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    
    # Media
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    image_url = models.URLField(blank=True, help_text="External image URL if not uploading")
    
    # Relationships
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    tags = models.ManyToManyField(Tag, blank=True, related_name='products')
    
    # Product Details
    badge_text = models.CharField(max_length=100, blank=True, help_text="Badge text shown on product card")
    features = models.JSONField(default=list, blank=True, help_text="List of features/benefits")
    what_included = models.JSONField(default=list, blank=True, help_text="What's included in the bundle")
    perfect_for = models.JSONField(default=list, blank=True, help_text="Perfect for whom")
    
    # Status
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        
        # Calculate discount percentage if original_price is set
        if self.original_price and self.price:
            discount = ((self.original_price - self.price) / self.original_price) * 100
            self.discount_percentage = int(discount)
        
        super().save(*args, **kwargs)

    @property
    def display_image(self):
        """Return image URL (uploaded or external)"""
        if self.image:
            return self.image.url
        return self.image_url or ''


class Order(models.Model):
    """Order/Checkout Model"""
    ORDER_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('cancelled', 'Cancelled'),
    ]

    # Customer Information
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=200, blank=True)
    
    # Order Details
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    
    # Pricing
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    # Bump Offer
    bump_offer_added = models.BooleanField(default=False)
    bump_offer_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    # Status
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='pending')
    payment_id = models.CharField(max_length=200, blank=True, help_text="Payment gateway transaction ID")
    
    # Download
    download_link = models.URLField(blank=True, help_text="Link sent to customer after payment")
    download_sent = models.BooleanField(default=False)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Order #{self.id} - {self.product.name} - {self.email}"

    def save(self, *args, **kwargs):
        # Calculate total amount
        self.total_amount = self.unit_price * self.quantity
        if self.bump_offer_added and self.bump_offer_price:
            self.total_amount += self.bump_offer_price
        super().save(*args, **kwargs)


class SiteSettings(models.Model):
    """Site-wide Settings Model"""
    site_name = models.CharField(max_length=200, default="SKILCART")
    site_tagline = models.CharField(max_length=200, default="Best Digital Product In India")
    
    # Contact Information
    whatsapp_number = models.CharField(max_length=20, default="919712237383")
    instagram_url = models.URLField(default="https://instagram.com/mr_sebby_yt")
    youtube_url = models.URLField(default="https://youtube.com/@mr_sebby")
    
    # Footer Links
    footer_links = models.JSONField(default=dict, blank=True)
    
    # SEO
    meta_description = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return "Site Settings"

    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        self.pk = 1
        super().save(*args, **kwargs)


