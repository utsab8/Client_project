"""
Management command to populate initial data for Skillcart
"""
from django.core.management.base import BaseCommand
from api.models import Product, Category, Tag, SiteSettings


class Command(BaseCommand):
    help = 'Populate initial data for Skillcart website'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting data population...'))

        # Create Site Settings
        settings, created = SiteSettings.objects.get_or_create(pk=1)
        if created:
            self.stdout.write(self.style.SUCCESS('Created site settings'))
        else:
            self.stdout.write(self.style.WARNING('Site settings already exist'))

        # Create Category
        category, created = Category.objects.get_or_create(
            name='Reels Bundle',
            defaults={'description': 'Premium viral reels content for social media growth'}
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created category: {category.name}'))

        # Create Tags
        tags_data = [
            'Viral Content',
            'Instagram Reels',
            'Social Media',
            'Content Bundle',
            'Digital Product'
        ]
        for tag_name in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created tag: {tag.name}'))

        # Create Products based on existing HTML files
        products_data = [
            {
                'name': 'USA Reels Bundle',
                'slug': 'usa-reels-bundle',
                'price': 149,
                'original_price': 1490,
                'badge_text': 'USA Reels Bundle',
                'short_description': 'Premium USA reels content for viral social media growth',
                'description': 'Get access to premium USA reels bundle package perfect for viral social media growth. This comprehensive bundle includes high-quality, ready-to-post content that will save you hours of content creation time.',
                'features': [
                    'Premium trending content',
                    'Save hours of content creation',
                    'Boost engagement and watch time',
                    'Grow your following fast',
                    'Affordable pricing with 90% OFF'
                ],
                'what_included': [
                    'All complete bundle package',
                    'HD quality videos ready to post',
                    'Trending content for maximum engagement',
                    'Instant download access',
                    'Lifetime updates'
                ],
                'perfect_for': [
                    'Instagram Reels creators',
                    'YouTube Shorts channels',
                    'TikTok content creators',
                    'Social media managers',
                    'Digital marketers'
                ],
                'is_featured': False
            },
            {
                'name': 'Funny Comments Reels Bundle',
                'slug': 'funny-comments-bundle',
                'price': 99,
                'original_price': 990,
                'badge_text': 'Funny Comments Reels Bundle',
                'short_description': 'Viral funny comments reels for maximum engagement',
                'description': 'Get access to premium funny comments reels bundle package perfect for viral social media growth.',
                'features': ['Premium trending content', 'Save hours of content creation', 'Boost engagement'],
                'what_included': ['HD quality videos', 'Instant download access', 'Lifetime updates'],
                'perfect_for': ['Instagram Reels creators', 'Social media managers'],
                'is_featured': False
            },
            {
                'name': 'AI Funny Story Reels Bundle',
                'slug': 'ai-funny-story-bundle',
                'price': 199,
                'original_price': 1990,
                'badge_text': 'AI Funny Story Reels Bundle',
                'short_description': 'AI-generated funny story reels for viral content',
                'description': 'Get access to premium AI funny story reels bundle package perfect for viral social media growth.',
                'features': ['Premium trending content', 'Save hours of content creation', 'Boost engagement'],
                'what_included': ['HD quality videos', 'Instant download access', 'Lifetime updates'],
                'perfect_for': ['Instagram Reels creators', 'Social media managers'],
                'is_featured': False
            },
            {
                'name': '3500 Prank Video Reels Bundle',
                'slug': 'prank-video-bundle',
                'price': 249,
                'original_price': 2490,
                'badge_text': '3500 Prank Video Reels Bundle',
                'short_description': 'Massive collection of prank video reels',
                'description': 'Get access to 3500 prank video reels bundle package perfect for viral social media growth.',
                'features': ['Premium trending content', 'Save hours of content creation', 'Boost engagement'],
                'what_included': ['HD quality videos', 'Instant download access', 'Lifetime updates'],
                'perfect_for': ['Instagram Reels creators', 'Social media managers'],
                'is_featured': False
            },
            {
                'name': '1500+ Ai Hot Model Reels Bundle',
                'slug': 'ai-hot-model-bundle',
                'price': 199,
                'original_price': 1990,
                'badge_text': '1500+ Ai Hot Model Reels Bundle',
                'short_description': 'AI-generated hot model reels for viral content',
                'description': 'Get access to 1500+ AI hot model reels bundle package perfect for viral social media growth.',
                'features': ['Premium trending content', 'Save hours of content creation', 'Boost engagement'],
                'what_included': ['HD quality videos', 'Instant download access', 'Lifetime updates'],
                'perfect_for': ['Instagram Reels creators', 'Social media managers'],
                'is_featured': False
            },
            {
                'name': 'Bike Rider Reels Bundle',
                'slug': 'bike-rider-bundle',
                'price': 149,
                'original_price': 1490,
                'badge_text': 'Bike Rider Reels Bundle',
                'short_description': 'Premium bike rider reels for viral content',
                'description': 'Get access to premium bike rider reels bundle package perfect for viral social media growth.',
                'features': ['Premium trending content', 'Save hours of content creation', 'Boost engagement'],
                'what_included': ['HD quality videos', 'Instant download access', 'Lifetime updates'],
                'perfect_for': ['Instagram Reels creators', 'Social media managers'],
                'is_featured': False
            },
            {
                'name': 'Car Reels Bundle',
                'slug': 'car-reels-bundle',
                'price': 149,
                'original_price': 1490,
                'badge_text': 'Car Reels Bundle',
                'short_description': 'Premium car reels for viral content',
                'description': 'Get access to premium car reels bundle package perfect for viral social media growth.',
                'features': ['Premium trending content', 'Save hours of content creation', 'Boost engagement'],
                'what_included': ['HD quality videos', 'Instant download access', 'Lifetime updates'],
                'perfect_for': ['Instagram Reels creators', 'Social media managers'],
                'is_featured': False
            },
            {
                'name': 'Football Reels Bundle',
                'slug': 'football-reels-bundle',
                'price': 99,
                'original_price': 990,
                'badge_text': 'Football Reels Bundlle',
                'short_description': 'Premium football reels for viral content',
                'description': 'Get access to premium football reels bundle package perfect for viral social media growth.',
                'features': ['Premium trending content', 'Save hours of content creation', 'Boost engagement'],
                'what_included': ['HD quality videos', 'Instant download access', 'Lifetime updates'],
                'perfect_for': ['Instagram Reels creators', 'Social media managers'],
                'is_featured': False
            },
            {
                'name': '1000+ Doraemon Reels Bundle',
                'slug': 'doraemon-bundle',
                'price': 149,
                'original_price': 1490,
                'badge_text': '1000+ Doraemon Reels Bundle',
                'short_description': 'Massive Doraemon reels collection',
                'description': 'Get access to 1000+ Doraemon reels bundle package perfect for viral social media growth.',
                'features': ['Premium trending content', 'Save hours of content creation', 'Boost engagement'],
                'what_included': ['HD quality videos', 'Instant download access', 'Lifetime updates'],
                'perfect_for': ['Instagram Reels creators', 'Social media managers'],
                'is_featured': False
            },
            {
                'name': '1000+ Ai Superhero Interview Video clips Pack',
                'slug': 'ai-superhero-bundle',
                'price': 199,
                'original_price': 1990,
                'badge_text': '1000+ Ai Superhero Interview Video clips Pack',
                'short_description': 'AI superhero interview video clips',
                'description': 'Get access to 1000+ AI superhero interview video clips pack perfect for viral social media growth.',
                'features': ['Premium trending content', 'Save hours of content creation', 'Boost engagement'],
                'what_included': ['HD quality videos', 'Instant download access', 'Lifetime updates'],
                'perfect_for': ['Instagram Reels creators', 'Social media managers'],
                'is_featured': False
            },
            {
                'name': '2000+ PUBG Gameplay Reels Bundle',
                'slug': 'pubg-gameplay-bundle',
                'price': 249,
                'original_price': 2490,
                'badge_text': '2000+ PUBG Gameplay Reels Bundle',
                'short_description': 'Massive PUBG gameplay reels collection',
                'description': 'Get access to 2000+ PUBG gameplay reels bundle package perfect for viral social media growth.',
                'features': ['Premium trending content', 'Save hours of content creation', 'Boost engagement'],
                'what_included': ['HD quality videos', 'Instant download access', 'Lifetime updates'],
                'perfect_for': ['Instagram Reels creators', 'Social media managers'],
                'is_featured': False
            },
            {
                'name': 'Combo Reels bundle',
                'slug': 'combo-bundle',
                'price': 499,
                'original_price': 4999,
                'badge_text': 'Combo Reels bundle',
                'short_description': 'Complete all-in-one reels bundle package',
                'description': 'Get access to All premium complete bundle package perfect for viral social media growth. This comprehensive bundle includes high-quality, ready-to-post content that will save you hours of content creation time.',
                'features': [
                    'Premium trending content',
                    'Save hours of content creation',
                    'Boost engagement and watch time',
                    'Grow your following fast',
                    'Affordable pricing with 90% OFF'
                ],
                'what_included': [
                    'All complete bundle package',
                    'HD quality videos ready to post',
                    'Trending content for maximum engagement',
                    'Instant download access',
                    'Lifetime updates'
                ],
                'perfect_for': [
                    'Instagram Reels creators',
                    'YouTube Shorts channels',
                    'TikTok content creators',
                    'Social media managers',
                    'Digital marketers'
                ],
                'is_featured': True
            },
        ]

        # Get tags for products
        viral_tag = Tag.objects.get(name='Viral Content')
        reels_tag = Tag.objects.get(name='Instagram Reels')
        social_tag = Tag.objects.get(name='Social Media')
        bundle_tag = Tag.objects.get(name='Content Bundle')

        # Create Products
        for product_data in products_data:
            product, created = Product.objects.get_or_create(
                slug=product_data['slug'],
                defaults={
                    'name': product_data['name'],
                    'price': product_data['price'],
                    'original_price': product_data['original_price'],
                    'badge_text': product_data['badge_text'],
                    'short_description': product_data['short_description'],
                    'description': product_data['description'],
                    'features': product_data['features'],
                    'what_included': product_data['what_included'],
                    'perfect_for': product_data['perfect_for'],
                    'category': category,
                    'is_featured': product_data['is_featured'],
                }
            )
            if created:
                # Add tags
                product.tags.add(viral_tag, reels_tag, social_tag, bundle_tag)
                self.stdout.write(self.style.SUCCESS(f'Created product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.name}'))

        self.stdout.write(self.style.SUCCESS('\nData population completed successfully!'))


