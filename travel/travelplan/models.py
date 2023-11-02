from django.conf import settings
from django.db import models

from django.contrib.auth.models import User
from user_app.models import CustomUser


class PostPlan(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    view = models.IntegerField(default=0)
    location = models.CharField(max_length=20, null=True)
    status = models.CharField(max_length=30, null=True)
    traveldate = models.CharField(max_length=30, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    postimage = models.ImageField(
        upload_to="img/%Y/%m/%d",
        height_field=None,
        width_field=None,
        max_length=None,
        null=True,
        blank=True,
    )


class Comment(models.Model):
    post_plan = models.ForeignKey(PostPlan, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user_comments")
    comment = models.TextField(max_length=300)
    chrmt_upload_date = models.DateTimeField(auto_now_add=True)
    like_cnt = models.IntegerField(default=0, null=True)


class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post_plan = models.ForeignKey(PostPlan, on_delete=models.CASCADE, related_name="likes")
    like_upload_date = models.DateTimeField(auto_now_add=True)
