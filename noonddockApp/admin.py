from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'recommend')

admin.site.register(Post, PostAdmin)

# class PhotoAdmin(admin.ModelAdmin):
#     list_display = ('image', 'post_id')

# admin.site.register(Photo, PhotoAdmin)