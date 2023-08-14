from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from noonddockApp.views import main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('accounts/', include('accounts.urls',namespace='accounts')),
    path('family/', include('family.urls',namespace='family')),
    path('noonddock/', include('noonddockApp.urls',namespace='noonddockApp')),
] 
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)
