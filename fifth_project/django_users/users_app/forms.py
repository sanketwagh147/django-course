from dataclasses import fields

from django.contrib.auth.models import User
from django.forms import ModelForm
from users_app.models import UserProfileInfo

from django import forms


class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "email", "password")


class UserProfileInfoForm(ModelForm):
    ...

    class Meta:
        model = UserProfileInfo
        fields = ("portfolio_site", "profile_pic")
