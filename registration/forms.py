from django import forms
from django.utils.translation import ugettext_lazy as _
from registration.models import *
from django.forms.models import ModelForm
from django.contrib import admin

class UserRegistrationForm(ModelForm):
    repass = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Re Enter Password',
    'min_length':1, 'max_length':20}))