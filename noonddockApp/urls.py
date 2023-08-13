from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import main, post_list_view, post_inform 

app_name = 'noonddockApp'

urlpatterns = [
    path('post_list', post_list_view, name='post_list'), #눈똑 리스트
    path('inform/<int:post_id>', post_inform, name='inform'), #눈똑 상세페이지 id당 하나씩
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
