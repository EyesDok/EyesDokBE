from django.contrib import admin
from .models import Post,Image

class ImageInline(admin.TabularInline):  # TabularInline 또는 StackedInline 사용
    model = Image
    extra = 3  # 한 번에 업로드 가능한 이미지 수 (여기서는 3개)

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'pub_date','like_count')
    list_filter = ['pub_date']
    inlines = [ImageInline]


admin.site.register(Post, PostAdmin)

# class PhotoAdmin(admin.ModelAdmin):
#     list_display = ('image', 'post_id')

# admin.site.register(Photo, PhotoAdmin)