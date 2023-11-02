from django.shortcuts import render, redirect, get_object_or_404
from .models import PostPlan, Comment
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm

from django.urls import reverse

import pdfkit
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.views import View


from django.http import JsonResponse
from .models import Like

# Create your views here.


def main(request):
    list_post = PostPlan.objects.all().order_by("-view")
    return render(request, "travel_app/main.html", {"posts": list_post})


@login_required
def write(request, post_id=None):
    post = None
    if post_id:
        try:
            post = PostPlan.objects.get(id=post_id)
        except PostPlan.DoesNotExist:
            pass
    context = {"post": post}
    return render(request, "travel_app/write.html", context)


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  # 임시 저장
            post.author_id = request.user.id
            post.location = request.POST.get("location", "")
            post.status = request.POST.get("status", "")
            post.traveldate = request.POST.get("traveldate", "")
            if "postimage" in request.FILES:
                post.postimage = request.FILES["postimage"]
            else:
                post.postimage = None
            post.save()  # 최종 저장
            return redirect("travel_app:main_post", pk=post.pk)  # 저장 후 상세 페이지로 이동
        else:
            print(form.errors)  # 에러출력추가
    else:
        form = PostForm()
    return render(request, "travel_app/main.html", {"form": form})


# 게시글 상세보기
def main_post(request, pk):
    # poss id 번호 불러옴
    post = get_object_or_404(PostPlan, pk=pk)
    if request.method == "POST":
        # html에서 delete-button name의 인풋을 눌러서 작동
        if "delete-button" in request.POST:
            post.delete()
            return render(request, "travel_app/main.html")
    #  조회수 증가
    post.view += 1
    post.save()
    comments = Comment.objects.all().order_by("-chrmt_upload_date")

    context = {"post": post, "comments": comments}

    return render(request, "travel_app/main_post.html", context)


# 수정하기
def edit_post(request, post_id):
    post = get_object_or_404(PostPlan, id=post_id)
    if post:
        post.description = post.description.strip()
    if request.method == "POST":
        post.title = request.POST.get("title", "")
        post.description = request.POST.get("description", "")
        post.status = request.POST.get("status", "")
        post.location = request.POST.get("location", "")
        post.traveldate = request.POST.get("traveldate", "")
        if "postimage" in request.FILES:
            post.postimage = request.FILES["postimage"]
        post.save()
        return redirect("travel_app:main_post", pk=post_id)
    context = {"post": post}

    return render(request, "travel_app/write.html", context=context)


# 삭제하기
@login_required
def post_delete(request, pk):
    post = get_object_or_404(PostPlan, pk=pk)

    if request.user != post.author:
        return redirect("travel_app:main", pk=post.pk)

    if request.method == "POST":
        post.delete()
        return redirect("travel_app:main")

    return render(request, "travel_app/main.html", {"post": post})


# 댓글달기
def add_comment(request, post_id):
    post = get_object_or_404(PostPlan, id=post_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_plan = post
            comment.user = request.user
            comment.save()

            # 댓글을 저장한 후 해당 게시물 상세 페이지로 리디렉션
            return redirect(reverse("travel_app:main_post", args=[post_id]))
    else:
        form = CommentForm()

    # 댓글 작성에 실패하면 여기로 돌아갈 수 있도록 설정할 수 있습니다.
    return redirect(reverse("travel_app:main_post", args=[post_id]))


# PDF변환 #장고에서는 사용이어렵다
class HTMLToPDFView(View):
    def get(self, request, pk, *args, **kwargs):
        # 특정 PostPlan 객체 불러오기
        post = get_object_or_404(PostPlan, pk=pk)

        # HTML 템플릿 렌더링
        html_string = render_to_string("travel_app/main_post.html", {"post": post})

        # wkhtmltopdf의 경로 설정 및 옵션 설정
        config = pdfkit.configuration(
            wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
        )
        options = {"no-images": None, "debug-javascript": None}

        # HTML을 PDF로 변환
        pdf = pdfkit.from_string(html_string, False, options=options, configuration=config)

        # PDF 파일 응답 생성
        response = HttpResponse(pdf, content_type="application/pdf")
        response["Content-Disposition"] = 'attachment; filename="output.pdf"'

        return response


# 좋아요~
def like_post(request, post_id):
    post = get_object_or_404(PostPlan, id=post_id)
    user = request.user

    if request.method == "POST":
        if post.likes.filter(user=user).exists():  # 이미 좋아요를 눌렀다면
            post.likes.filter(user=user).delete()  # 좋아요 취소
            result = post.likes.count()  # 좋아요 개수 업데이트
            return JsonResponse({"result": result})  # 좋아요 개수 반환
        else:
            Like.objects.create(user=user, post_plan=post)  # 좋아요
            result = post.likes.count()  # 좋아요 개수 업데이트
            return JsonResponse({"result": result})  # 좋아요 개수 반환
