from django import forms
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from .models import User
class UserCreateForm(UserCreationForm):
    # password1 = forms.CharField(
    #     label='Password', widget=forms.PasswordInput())
    # password2 = forms.CharField(
    #     label='Confirm Password(again)', widget=forms.PasswordInput())

    class Meta:
        fields=('fullname','username','email','country','password1','password2')
        model=User
        help_texts = {
            'username': None,
        }
        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            self.fields['username'].label=""
            self.fields['email'].label=""
