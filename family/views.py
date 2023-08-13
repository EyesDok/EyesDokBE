from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from .models import Family


def myFamily_view(request):
    user = CustomUser.objects.get(username=request.user.username)
    families = user.families.all()
    return render(request, 'family/MyFamily.html',{'families': families})

@login_required
def create_family_view(request):
    if request.method == 'POST':
        familyname = request.POST.get('familyname')
        members = request.POST.get('members')
        family = Family.objects.create(familyname=familyname, members=members)
        family.users.add(request.user) # 현재 로그인한 사용자를 가족 그룹에 추가
        return redirect('family:myFamily')  # 가족 그룹 목록 페이지로 리다이렉트
    return render(request, 'family/Family.html')