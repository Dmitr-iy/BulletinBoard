from django import forms

from ckeditor.widgets import CKEditorWidget

from .models import (Post, Reply, User)


class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ['title', 'content', 'categories']
        labels = {
            'title': 'Title',
            'content': 'Content posted',
            'categories': 'Categories',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Your title',
                'class': 'form-text',
            }),
            'content': forms.CharField(widget=CKEditorWidget())
        }


class ReplyForm(forms.ModelForm):
    class Meta():
        model = Reply
        fields = ['content']
        labels = {
            'content': '',
        }
        widgets = {
            'content': forms.TextInput(attrs={
                'placeholder': 'Your response',
                'class': 'form-reply',
            }),
        }


class ReplyApproveForm(forms.ModelForm):
    class Meta():
        model = Reply
        fields = ['approved']
        labels = {
            'approved': 'Approve the response',
        }


class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username': 'Username',
            'first_name': 'Name',
            'last_name': 'Lastname',
            'email': 'email',
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Your username',
                'class': 'form-text',
            }),
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Your name',
                'class': 'form-text',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Your Lastname',
                'class': 'form-text',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Your email address',
                'class': 'form-text',
            }),
        }
