from django import forms
from .models import PostPlan, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = PostPlan
        fields = ["title", "description", "postimage"]