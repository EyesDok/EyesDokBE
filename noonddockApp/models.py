from django.db import models
from accounts.models import CustomUser

class Post(models.Model):
    content     =   models.TextField("CONTENT", max_length=300, default="포스트 내용") #포스트 내용
    title       =   models.CharField("TITLE", max_length=20, default="포스트 제목") #포스트 제목
    pub_date    =   models.DateField("PUB_DATE", auto_now_add=True) #작성일자
    image       =   models.ImageField("IMAGE", upload_to="postImage/", default="static/img/defaultImg.png") #포스트 사진
    user        =   models.ForeignKey(CustomUser, on_delete=models.CASCADE) #UserFK
    like_users  =   models.ManyToManyField(CustomUser, related_name='like_posts', blank=True) #게시물과 사용자 다대다 관계 구성
    like_count  =   models.PositiveIntegerField("LIKE_COUNT", default=0) #좋아요 수
    category    =   models.IntegerField(verbose_name='테마',blank=True, null=True)
    #카테고리 (0:뮤지컬, 1:연극, 2:등산, 3:낚시)
    location    =   models.TextField("LOCATION", max_length=300, default="위치") # 위치
    parking     =   models.TextField("PARKING", max_length=300, default="주차")  # 주차
    summary     =   models.TextField("SUMMARY", max_length=300, default="한줄 눈똑") # 한줄 눈똑
    reservation =   models.TextField("RESERVATION", max_length=300, default="예약") # 예약
    class Meta:
        db_table = 'post'

    def __str__(self):
        return self.title
    
class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')  # 'images'는 역참조 이름
    image = models.ImageField(upload_to='postImages/')



    def __str__(self):
        return f"Image for {self.post.title}"

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


class Comment(models.Model):
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    post = models.ForeignKey(to='Post', on_delete=models.CASCADE)
    writer = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, null=True, blank=True)

