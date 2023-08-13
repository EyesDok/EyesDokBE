from django.shortcuts import render

from noonddockApp.models import Post, Save

# Create your views here.
def main(request):
    return render(request, 'main.html')

#눈똑 리스트
def post_list_view(request):

    #추천수 기준 내림차순 정렬 상위 4개 게시물
    post_title_list = Post.objects.all().order_by('-recommend')[:4]
    
    #게시글 작성일 기준 내림차순 정렬 (선택)'최신순'
    if request.GET.get('order') == 'recent':        
        post_list = Post.objects.all().order_by('-pub_date') 

    #게스글 추천수 기준 내림차순 정렬 (선택) '인기순'
    elif request.GET.get('order') == 'popular':
        post_list = Post.objects.all().order_by('-recommend')
        
    else:
        post_list = Post.objects.all()
    if request.user.is_authenticated:
        for post in post_list:
            post.is_recommened = post.save_set.filter(user=request.user).exists()

    context ={
            'post_list': post_list,
            'post_title_list' : post_title_list,
        }
    
    return render(request, 'main/post-list.html', context)


#추천=눈똑수
def post_recommend_view(request, id):
    if request.user.is_authenticated:
        post = get_object_or_404(post, id=id)
        user = request.user

    # 이미 좋아요를 눌렀는지 확인
        if Save.objects.filter(user=user, post=post).exists():
            # 이미 좋아요를 눌렀을 경우 처리
            save = Favorite.objects.get(user=user, post=post)
            save.delete()
            # 좋아요 개수를 1 증가시킴
            post.like -= 1
            post.save()

        else:
            # 중개 모델을 생성하고 저장
            like = Save(user=user, post=post)
            like.save()

            # 좋아요 개수를 1 증가시킴
            post.like += 1
            post.save()

        return redirect('posts:post-list')
        
    return redirect('accouts:login')