from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        error_messages={
            'required': '제목을 꼭 입력해주세요.',
            'min_length': '제목은 최소 2자 이상이어야 합니다.',
        },
        min_length=2,
    )

    content = forms.CharField(
        required=True,
        error_messages={
            'required': '내용을 입력해주세요.',
            'min_length': '내용은 최소 3자 이상이어야 합니다.',
        },
        min_length=3,
        widget=forms.Textarea,
    )

    class Meta:
        model = Todo
        fields = ['title', 'content']