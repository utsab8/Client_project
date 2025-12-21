from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from api.views_frontend import index, product, checkout

print("INFO: Loading urls_fixed.py")

urlpatterns = [
    # Frontend pages
    path('', index, name='index'), 
    path('home/', index, name='home'),
    path('product.html', product, name='product'),
    path('checkout.html', checkout, name='checkout'),
    
    # Admin and API
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
