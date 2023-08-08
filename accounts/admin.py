from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# CustomUser를 위한 커스텀 어드민 클래스 정의
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'membership']  # 여기서 'membership' 필드를 추가
    list_filter = ['is_staff', 'is_superuser', 'is_active', 'groups']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('membership',)}),
    )

# CustomUserAdmin 클래스를 CustomUser 모델에 등록
admin.site.register(CustomUser, CustomUserAdmin)