from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "travel_app"
urlpatterns = [
    path("", views.main, name="main"),
    
    path("wirte/", views.write, name="write"),

]