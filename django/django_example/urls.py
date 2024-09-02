from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
 
from django.urls import path, include

urlpatterns = [
    path('', include("mydjango.urls")),
    path('admin/', admin.site.urls),
    path('menu/',include('menu.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    