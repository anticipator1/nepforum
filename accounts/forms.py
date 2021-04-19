from django.forms import ModelForm,Textarea
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

#class CommentForm(ModelForm):
    #class Meta:
       # model=AddComment
        #fields=['comment','post']
class UserForm(ModelForm):
    class Meta:
        model=Forum_Users
        fields='__all__'
        exclude=['user']


class CreatePost(ModelForm):



    class Meta:
        model=Post
        fields='__all__'
        category = forms.CharField(widget=forms.CharField, disabled=True)


        widgets = {'forum_user': forms.HiddenInput(),
                   'description': Textarea(attrs={'cols': 80, 'rows': 40,'style':'height:300px'}),
                   }


class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class CommentForm(ModelForm):


    class Meta:
        model=AddComment
        fields='__all__'
        exclude=['pic','hker']
        forum_user=forms.CharField(disabled=True)
        widgets = {
            'forum_user': forms.HiddenInput(),
                   'comment': Textarea(attrs={'cols': 80, 'rows': 40, 'style': 'height:300px'}),
                   }

