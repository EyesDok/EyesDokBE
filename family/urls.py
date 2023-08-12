from django.urls import path
from .views import myFamily_view
# from .views import 

app_name = 'family'

urlpatterns = [
    path('', myFamily_view, name='myFamily'),
    # path('login/', login_view, name='login'),
    # path('logout/', logout_view, name='logout'),
    # path('check-username/', check_username_view, name='check-username'),
]