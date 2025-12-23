"""
Utility functions for the API app
"""
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags
from .models import SiteSettings


def _email_context():
    settings_obj, _ = SiteSettings.objects.get_or_create(pk=1)
    support_email = settings_obj.support_email or getattr(settings, 'SUPPORT_EMAIL', '')
    from_email = settings_obj.from_email or getattr(settings, 'DEFAULT_FROM_EMAIL', support_email)
    return settings_obj, support_email, from_email


def send_order_confirmation_email(order):
    """
    Send order confirmation email to customer
    
    Args:
        order: Order instance
    """
    try:
        settings_obj, support_email, from_email = _email_context()
        subject = f'Order Confirmation - Order #{order.id} - {settings.SITE_NAME}'
        
        # Prepare context for email template
        context = {
            'order': order,
            'product': order.product,
            'site_name': settings.SITE_NAME,
            'site_url': settings.SITE_URL,
            'support_email': support_email,
        }
        
        # Render HTML email
        html_message = render_to_string('emails/order_confirmation.html', context)
        
        # Plain text version (strip HTML tags)
        plain_message = strip_tags(html_message)
        
        # Send email
        send_mail(
            subject=subject,
            message=plain_message,
            from_email=from_email,
            recipient_list=[order.email],
            html_message=html_message,
            fail_silently=False,
        )
        
        return True
    except Exception as e:
        print(f"Error sending order confirmation email: {e}")
        return False


def send_download_link_email(order):
    """
    Send download link email to customer after payment
    
    Args:
        order: Order instance with download_link
    """
    if not order.download_link:
        return False
        
    try:
        settings_obj, support_email, from_email = _email_context()
        subject = f'Download Link - Order #{order.id} - {settings.SITE_NAME}'
        
        # Prepare context for email template
        context = {
            'order': order,
            'product': order.product,
            'site_name': settings.SITE_NAME,
            'site_url': settings.SITE_URL,
            'support_email': support_email,
        }
        
        # Render HTML email
        html_message = render_to_string('emails/download_link.html', context)
        
        # Plain text version
        plain_message = strip_tags(html_message)
        
        # Send email
        send_mail(
            subject=subject,
            message=plain_message,
            from_email=from_email,
            recipient_list=[order.email],
            html_message=html_message,
            fail_silently=False,
        )
        
        # Mark as sent
        order.download_sent = True
        order.save(update_fields=['download_sent'])
        
        return True
    except Exception as e:
        print(f"Error sending download link email: {e}")
        return False


def send_payment_verified_email(order):
    """
    Send payment verified email to customer
    """
    try:
        settings_obj, support_email, from_email = _email_context()
        subject = f'Payment Verified - Order #{order.id} - {settings.SITE_NAME}'
        context = {
            'order': order,
            'product': order.product,
            'site_name': settings.SITE_NAME,
            'site_url': settings.SITE_URL,
            'support_email': support_email,
        }
        html_message = render_to_string('emails/payment_verified.html', context)
        plain_message = strip_tags(html_message)
        send_mail(
            subject=subject,
            message=plain_message,
            from_email=from_email,
            recipient_list=[order.email],
            html_message=html_message,
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f"Error sending payment verified email: {e}")
        return False

