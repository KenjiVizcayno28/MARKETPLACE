from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import *
from django.forms import CharField

class RegisterForm(forms.Form):
    username = CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter your email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter your password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter your password again'}))

def clean_username(self):
    username = self.cleaned_data['username']
    if User.objects.filter(username=username).exists():
        raise forms.ValidationError("Username already exists")
    return username

def clean_email(self):
    email = self.cleaned_data['email']
    if User.objects.filter(email=email).exists():
        raise forms.ValidationError("Email already exists")
    return email

def clean(self):
    password = self.cleaned_data.get['password']
    password2 = self.cleaned_data.get['password2']
    if self.cleaned_data['password'] != password2:
        raise forms.ValidationError("Password don't match")
    return password
