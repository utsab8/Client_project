from django.contrib import admin
from django.urls import path, include
from django.shortcuts import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

# Debug view
def debug_home(request):
    return HttpResponse("<h1>Homepage is Working!</h1>")

from api.views_frontend import index, product, checkout, payment, success, privacy_policy, terms_conditions, refund_policy

urlpatterns = [
    # Debug path
    path('debug/', debug_home),
    
    # Real paths
    path('', index, name='index'),
    path('home/', index, name='home'),
    path('product.html', product, name='product'),
    path('checkout.html', checkout, name='checkout'),
    path('payment.html', payment, name='payment'),
    path('success.html', success, name='success'),
    path('privacy-policy.html', privacy_policy, name='privacy'),
    path('terms-and-conditions.html', terms_conditions, name='terms'),
    path('refund-policy.html', refund_policy, name='refund'),

    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    # In production, serve media files through your web server (nginx/apache)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

print(f"DEBUG: Final urlpatterns count: {len(urlpatterns)}")


