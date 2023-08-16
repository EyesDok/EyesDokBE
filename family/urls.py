from django.urls import path
from .views import myFamily_view ,create_family_view,chat_view

app_name = 'family'

urlpatterns = [
    path('', myFamily_view, name='myFamily'),
    path('create/', create_family_view, name='createFamily'),
    path('chat/',chat_view, name='chat'),
]