from django.contrib import admin
from django.urls import path, include
from django.shortcuts import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

# Debug view
def debug_home(request):
    return HttpResponse("<h1>Homepage is Working!</h1>")

from api.views_frontend import index, product, checkout

urlpatterns = [
    # Debug path
    path('debug/', debug_home),
    
    # Real paths
    path('', index, name='index'),
    path('home/', index, name='home'),
    path('product.html', product, name='product'),
    path('checkout.html', checkout, name='checkout'),

    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

print(f"DEBUG: Final urlpatterns count: {len(urlpatterns)}")


