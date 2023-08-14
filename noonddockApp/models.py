from django.db import models
from accounts.models import CustomUser


class Post(models.Model):
    content     =   models.TextField("CONTENT", max_length=300, default="포스트 내용") #포스트 내용
    title       =   models.CharField("TITLE", max_length=20, default="포스트 제목") #포스트 제목
    pub_date    =   models.DateField("PUB_DATE", auto_now_add=True) #작성일자
    image       =   models.ImageField("IMAGE", upload_to="postImage/", default="static/img/defaultImg.png") #포스트 사진
    user        =   models.ForeignKey(CustomUser, on_delete=models.CASCADE) #UserFK
    category    =   models.PositiveIntegerField("CATEGORY") #카테고리
    like_count  =   models.PositiveIntegerField("LIKE_COUNT", default=0) # 좋아요 수
    class Meta:
        db_table = 'post'

    def __str__(self):
        return self.title

class Like(models.Model):
    user        =   models.ForeignKey(CustomUser, on_delete=models.CASCADE) #UserFK
    post        =   models.ForeignKey(Post, on_delete=models.CASCADE, default=1) #PostFK
    pub_date    =   models.DateField("PUB_DATE", auto_now_add=True) #작성일자

    #Save 모델의 데이터베이스 테이블에 대해, user 필드와 post 필드의 조합이 고유하게 유지
    def save(self, *args, **kwargs):
        super(Like, self).save(*args, **kwargs)
        self.post.like_count = self.post.like_set.count()  # 좋아요 개수 업데이트
        self.post.save()
        
    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user.username} likes {self.post.title}"
