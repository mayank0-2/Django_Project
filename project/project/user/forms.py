from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from user.models import post

class UserRegisterForm (UserCreationForm) :
    email = forms.EmailField()    


    class meta : 
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PostForm (forms.ModelForm):

    class Meta:
        model = post 
        fields = ['user_name', 'post_title', 'post_content', 'date_published', 'user_profile_link']

