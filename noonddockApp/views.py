from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from noonddockApp.models import Post, Like
from django.http import JsonResponse

# Create your views here.

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
@login_required
def liked_post(request, id):
    if request.user.is_authenticated:
        post = get_object_or_404(post, id=id)
        user = request.user

        if request.user in post.like_users.all():
            post.like_users.remove(request.user)
            post.like_count -= 1
        else:
            post.like_users.add(request.user)
            post.like_count += 1

        post.save()

        return redirect('NoonDDocklistPage/post_list.html')

    return redirect('accouts/login.html')
    

#js 토글 관련, js 잘 몰라서 그냥 냅두는 중
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    like, created = Like.objects.get_or_create(user=user, post=post)
    
    if not created:
        like.delete()
    
    like_count = post.like_set.count()
    liked = created
    
    return JsonResponse({'liked': liked, 'like_count': like_count})

#눈똑 상세 페이지
def post_inform(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    context = {
        'post': post,
    }
    
    return render(request, 'InformPage/Inform.html', context)

#메인 페이지
def main(request):
    post_list = Post.objects.all()

    if request.user.is_authenticated:
        user_liked = Like.objects.filter(user=request.user)
        for post in post_list:
            post.is_liked = user_liked.filter(post=post).exists()

    context = {
        'post_list' : post_list,
    }
    return render(request, 'MainPage/main.html', context)

#눈똑 페이지
def noonddock(request):
    post_list = Post.objects.all().order_by('-pub_date')[:4]

    if request.user.is_authenticated:
        user_liked = Like.objects.filter(user=request.user)
        for post in post_list:
            post.is_liked = user_liked.filter(post=post).exists()

    context = {
        'post_list' : post_list,
    }
    return render(request, 'NoonDDockPage/NoonDDock.html', context)

#나의 눈똑 페이지
def my_noonddock(request):
    post_title_list = Post.objects.all().order_by('-like_count')[:6]
    post_list = Post.objects.all().order_by('-like_count')[:6]

    if request.user.is_authenticated:
        for post in post_list:
            post.is_liked = post.like_set.filter(user=request.user).exists()

    context = {
        'post_list': post_list,
        'post_title_list' : post_title_list,
    }

    return render(request, 'MyNoonDDockPage/my_noonddock.html', context)
