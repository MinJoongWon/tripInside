from django.shortcuts import render, redirect, get_object_or_404
from .models import PostPlan, Comment
from django.contrib.auth.decorators import login_required
from .forms import PostForm
# Create your views here.

def main(request):
    list_post = PostPlan.objects.all().order_by("-view")
    return render(request, "travel_app/main.html", {"posts": list_post})

@login_required
def write(request, post_id=None):
    post = None
    if post_id:
        try:
            post = PostPlan.objects.get(id=post_id)  # 'PostProduct' 대신 'PostPlan'을 사용.
        except PostPlan.DoesNotExist:  # 'PostProduct' 대신 'PostPlan'을 사용.
            pass
    context = {"post": post}
    return render(request, "travel_app/write.html", context)


# 게시글 업로드
@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  # 임시 저장
            post.author_id = request.user.id
            post.save()  # 최종 저장
            return redirect("travel_app:main_post", pk=post.pk)  # 저장 후 상세 페이지로 이동
        else:
            print(form.errors)  # 에러출력추가
    else:
        form = PostForm()
    return render(request, "travel_app/main_post.html", {"form": form})

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  # 임시 저장
            post.author_id = request.user.id
            post.save()  # 최종 저장
            return redirect("travel:trade_post", pk=post.pk)  # 저장 후 상세 페이지로 이동
        else:
            print(form.errors)  # 에러출력추가
    else:
        form = PostForm()
    return render(request, "travel_app/main.html", {"form": form})

#게시글 상세보기
def main_post(request, pk):
    #poss id 번호 불러옴
    post = get_object_or_404(PostPlan, pk=pk)
    if request.method == "POST":
        # html에서 delete-button name의 인풋을 눌러서 작동
        if "delete-button" in request.POST:
            post.delete()
            # 포스트페이지로 가는게 맞아서 나중에 바꿀것
            # return redirect('dangun_app/trade')
            return render(request, "travel_app/main.html")
    #  조회수 증가
    post.view += 1
    post.save()
    comments = Comment.objects.filter(post=post).order_by("-created_date")

    # # 가장 최근 생성된 채팅방
    # recent_chatroom = ChatRoom.objects.filter(product_id=post.id).order_by("-created_at").first()

    context = {
        "post": post,
        "comments": comments,
        # "form": CommentForm(),
        # "recent_chatroom": recent_chatroom
    }

    return render(request, "travel_app/main_post.html", context)