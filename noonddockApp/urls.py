from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import main, post_list_view, post_inform, noonddock, my_noonddock, liked_post, update_like_count 

app_name = 'noonddockApp'

urlpatterns = [
    path('post_list_view', post_list_view, name='post_list_view'), #눈똑 리스트
    path('inform/<int:post_id>', post_inform, name='inform'), #눈똑 상세페이지 post_id당 하나씩
    path('', main, name='main'), #메인 페이지
    path('noonddock', noonddock, name='noonddock'), #눈똑 페이지
    path('my_noonddock', my_noonddock, name='my_noonddock'), #나의 눈똑 페이지
    path('liked_post/<int:post_id>', liked_post, name="liked_post"),
    path('update_like_count/', update_like_count, name='update_like_count'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
