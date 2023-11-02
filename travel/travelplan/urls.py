from django.contrib import admin
from django.urls import path, include
from . import views

# 클래스 기반 뷰는 as_view() 메소드 호출
# from .views import HTMLToPDFView

app_name = "travel_app"
urlpatterns = [
    path("", views.main, name="main"),
    path("wirte/", views.write, name="write"),
    path("main/<int:pk>", views.main_post, name="main_post"),
    path("create_form/", views.create_post, name="create_form"),
    path("edit/<int:post_id>/", views.edit_post, name="edit"),
    path("delete/<int:pk>/", views.post_delete, name="delete"),
    path("main_post/<int:post_id>", views.add_comment, name="add_comment"),
    path("like/<int:post_id>/", views.like_post, name="like_post"),
    # path("html_to_pdf/<int:pk>/", HTMLToPDFView.as_view(), name="html_to_pdf"),  # PDF 변환 URL 패턴 추가
]
