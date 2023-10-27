from django.conf import settings
from django.db import models

from django.contrib.auth.models import User
from user_app.models import CustomUser

# 포스트상품
class PostPlan(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    product = models.CharField(max_length=64, null=True, blank=True)
    description = models.TextField()
    view = models.IntegerField(default=0)
    status = models.CharField(max_length=1, default="N")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    postimage = models.ImageField(upload_to="img/%Y/%m/%d", height_field=None, width_field=None, max_length=None,)


class Comment(models.Model):
    post_plan = models.ForeignKey(PostPlan, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_comments')
    comment = models.TextField(max_length=300)
    chrmt_upload_date = models.DateTimeField(auto_now_add=True)
    like_cnt = models.IntegerField(default=0, null=True)

class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post_plan = models.ForeignKey(PostPlan, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    like_upload_date = models.DateTimeField(auto_now_add=True)