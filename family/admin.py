from django.contrib import admin
from .models import Family

@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display = ('familyname', 'members')