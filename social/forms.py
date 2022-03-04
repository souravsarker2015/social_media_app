from django import forms
from .models import Post, Comments, MessageModel


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
    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'multiple': True,

        })

    )

    class Meta:
        model = Post
        fields = ['body']


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


class ThreadForm(forms.Form):
    username = forms.CharField(label="", max_length=200)


class MessageForm(forms.ModelForm):
    body = forms.CharField(label="", max_length=2000)
    image = forms.ImageField(required=False)

    class Meta:
        model = MessageModel
        fields = ['body', 'image']
