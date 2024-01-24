from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserSite


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, max_length=100, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserSiteForm(forms.ModelForm):
    class Meta:
        model = UserSite
        fields = ['site_name']
