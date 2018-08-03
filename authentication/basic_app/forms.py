from basic_app import UserInfo
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        field = ('username','email','password')

class UserInfoForm(forms.ModelForm):

    class Meta():
        model = UserInfo
        field = ('profile_pic','portfolio')
