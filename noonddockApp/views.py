from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from noonddockApp.models import Post, Like

# Create your views here.
def main(request):
    return render(request, 'main.html')

#눈똑 게시글 리스트
def post_list_view(request):

    #추천수 기준 내림차순 정렬 상위 4개 게시물
    post_title_list = Post.objects.all().order_by('-like')[:12]
    
    #게시글 작성일 기준 내림차순 정렬 (선택)'최신순'
    if request.GET.get('order') == 'recent':        
        post_list = Post.objects.all().order_by('-pub_date') 

    #게스글 추천수 기준 내림차순 정렬 (선택) '인기순'
    elif request.GET.get('order') == 'popular':
        post_list = Post.objects.all().order_by('-like')
        
    else:
        post_list = Post.objects.all()
    if request.user.is_authenticated:
        for post in post_list:
            post.is_recommened = post.like_set.filter(user=request.user).exists()

    context ={
            'post_list': post_list,
            'post_title_list' : post_title_list,
        }
    
    return render(request, 'NoonDDocklistPage/post_list.html', context)


#좋아요 기능=눈똑수
def liked_post(request, id):
    if request.user.is_authenticated:
        post = get_object_or_404(post, id=id)
        user = request.user

    # 이미 좋아요를 눌렀는지 확인
        if Like.objects.filter(user=user, post=post).exists():
            # 이미 좋아요를 눌렀을 경우 처리
            like = Like.objects.get(user=user, post=post)
            like.delete()
            # 좋아요 개수를 1 증가시킴
            post.like -= 1
            post.like()

        else:
            # 중개 모델을 생성하고 저장
            like = Like(user=user, post=post)
            like.save()

            # 좋아요 개수를 1 증가시킴
            post.like_count += 1
            post.save()

        return redirect('NoonDDocklistPage/post_list.html')
        
    return redirect('accouts/login.html')

#눈똑 상세 페이지
def post_inform(request, post_id):
    post = get_object_or_404(Question, pk=post_id)
    category = question.category
    question.views += 1
    question.like()
    
    sameCategory = Question.objects.filter(category=category).exclude(pk=question_id).order_by("?")[:5]

    context = {
        'question': question,
        'sameCategory': sameCategory,
    }
    return render(request, 'communicationApp/question-detail.html', context)

#메인 페이지
def main(request):
    return render(request, 'MainPage/main.html')

#눈똑 페이지
def noonddock(request):
    return render(request, 'NoonDDockPage/NoonDDock.html')

#나의 눈똑 페이지
def my_noonddock(request):
    post_title_list = Post.objects.all().order_by('-recommend')[:6]
    post_list = Post.objects.all().order_by('-recommend')[:6]
    if request.user.is_authenticated:
        for post in post_list:
            post.is_recommened = post.recommend_set.filter(user=request.user).exists()

    context = {
        'post_list': post_list,
        'post_title_list' : post_title_list,
    }

    return render(request, 'MyNoonDDockPage/my_noonddock.html', context)
