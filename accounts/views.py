from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth import get_user_model, authenticate, login

User = get_user_model()

def signup_view(request):
    # POST 요청 시
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        # 시니어/자녀 정보 받아오기
        membership = request.POST.get('membership')

        # DB에 유저 추가
        user = CustomUser.objects.create_user(username=username, email=email, password=password1, membership=membership)
        user.save()

        # 회원가입 성공 시 로그인 페이지로 이동
        return redirect('accounts:login')
    # GET 요청 시
    return render(request, 'accounts/signup.html')

def login_view(request):
    error_message = None
    # POST 요청 시
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 사용자 정보 인증
        user = authenticate(request, username=username, password=password)

        # 인증이 성공한 경우
        if user is not None:
            # 세션 설정 및 로그인
            login(request, user)
            # 로그인 후 메인페이지로 이동
            return redirect('family:myFamily')

        # 인증이 실패한 경우
        else:
            # 에러 메시지 등을 사용자에게 보여줄 수 있음
            error_message = "아이디 또는 비밀번호가 올바르지 않습니다."

    # GET 요청 시
    return render(request, 'accounts/login.html', {'error_message': error_message})

# 로그아웃 기능은 Django에서 기본적으로 제공됩니다.
# 따로 구현할 필요 없이 장고의 logout 함수를 사용하면 됩니다.
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('main')  # 로그아웃 후 리다이렉트할 URL 설정 (여기서는 홈 페이지로 이동)