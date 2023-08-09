from django.db import models

class Post(models.Model):
    content     =   models.TextField("CONTENT", max_length=300, default="포스트 내용") #포스트 내용
    title       =   models.CharField("TITLE", max_length=20, default="포스트 제목") #포스트 제목
    pub_date    =   models.DateField("DATE", auto_now_add=True) #작성일자
    recommend   =   models.PositiveIntegerField("RECOMMEND", default=0) #추천수수집을 위한 모델

class Photo(models.Model):
    post_id     =   models.ForeignKey(Post, on_delete=models.CASCADE, default=1) #PostFK
    image       =   models.ImageField("IMAGE", upload_to="/", default="static/img/") #포스트 사진
