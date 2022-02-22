from django import forms
from .models import Post, Comments


class PostForm(forms.ModelForm):
    body = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={
                'rows': '3',
                'placeholder': 'Say something...',
            }
        )
    )
    image = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ['body', 'image']


class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={
                'rows': '2',
                'placeholder': 'Say comment...',
            }
        )
    )

    class Meta:
        model = Comments
        fields = ['comment']
