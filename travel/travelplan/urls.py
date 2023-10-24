from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "travel_app"
urlpatterns = [
    path("", views.main, name="main"),
    
    path("wirte/", views.write, name="write"),

    path("main/<int:pk>", views.main_post, name="main_post"),

    path("create_form/", views.create_post, name="create_form"),

]