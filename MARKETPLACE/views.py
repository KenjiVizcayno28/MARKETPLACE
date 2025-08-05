from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

from .forms import *
from .settings import   DEBUG

def marketplace(request):
    return render(request, 'base.html')

def register(request):
    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        username = register_form.cleaned_data.get('username')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        password2 = register_form.cleaned_data.get('password2')
        print(register_form.cleaned_data)
        context = {'register_form': register_form,}
    return render(request, 'auth/register.html')