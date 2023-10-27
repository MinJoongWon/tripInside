from django import forms
from .models import PostPlan, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = PostPlan
        fields = ["title", "description", "postimage"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        labels = {
            'comment': '',  # 'text' 필드의 라벨을 빈 문자열로 설정
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs.update({
            'class': 'form-text',
            'rows': '4',
            'cols': '100',
        })