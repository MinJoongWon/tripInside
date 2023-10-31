from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "travel_app"
urlpatterns = [
    path("", views.main, name="main"),
    path("wirte/", views.write, name="write"),
    path("main/<int:pk>", views.main_post, name="main_post"),
    path("create_form/", views.create_post, name="create_form"),
    path("edit/<int:post_id>/", views.edit_post, name="edit"),
    path("delete/<int:pk>/", views.post_delete, name="delete"),
    path("main_post/<int:post_id>", views.add_comment, name="add_comment"),
]
