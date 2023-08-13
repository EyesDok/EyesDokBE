from django.db import models

class Post(models.Model):
    content     =   models.TextField("CONTENT", max_length=300, default="포스트 내용") #포스트 내용
    title       =   models.CharField("TITLE", max_length=20, default="포스트 제목") #포스트 제목
    pub_date    =   models.DateField("PUB_DATE", auto_now_add=True) #작성일자
    recommend   =   models.PositiveIntegerField("RECOMMEND", default=0) #추천수수집을 위한 모델
    image       =   models.ImageField("IMAGE", upload_to="postImage/", default="static/img/defaultImg.png") #포스트 사진


    def __str__(self):
        return self.title

# class Photo(models.Model):
#     post_id     =   models.ForeignKey(Post, on_delete=models.CASCADE, default=1) #PostFK
#     image       =   models.ImageField("IMAGE", upload_to="postImage/", default="static/img/defaultImg.png") #포스트 사진
