from django.conf import settings
from django.db import models

from django.contrib.auth.models import User
from user_app.models import CustomUser

# 포스트상품
class PostProduct(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    # 물품정보는 현재 사용하지 않고 타이틀만 사용
    product = models.CharField(max_length=64, null=True, blank=True)
    description = models.TextField()
    price = models.IntegerField(default=0)
    view = models.IntegerField(default=0)
    status = models.CharField(max_length=1, default="N")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
