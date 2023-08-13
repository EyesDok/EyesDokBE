from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import main

app_name = 'noonddockApp'

urlpatterns = [
    path('main', main, name="main"),
]