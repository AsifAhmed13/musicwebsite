from django.shortcuts import render,redirect
from .models import Album
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib import messages
from .forms import NewLoginForm,NewSignUpForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

User = get_user_model()

def username_present(username):
    if User.objects.filter(username=username).exists():
        return True
    return False

def index(request):
    return render(request,"music/index.html",{
        "albums": Album.objects.all(),
    })

def login_view(request):
    form = NewLoginForm(request.POST or None)
    if(form.is_valid()):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username , password=password)
            if not user:
                messages.error(request , 'Incorrect Credentials')
                return redirect(login_view)
            if not user.check_password(password):
                messages.error(request , 'Incorrect Password')
                return redirect(login_view)
            if  not user.is_active:
                messages.error(request , 'User not active')
                return redirect(login_view)
        return redirect(index)
    return render(request, "music/login.html" , {
        "forms" : NewLoginForm
    })

def signup_view(request):
    form = NewSignUpForm(request.POST )
    if( form.is_valid()):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        reenterpassword = form.cleaned_data.get('reenterpassword')
        if password!=reenterpassword:
            messages.error(request , "Password did not match")
            return redirect(signup_view)
        if(username_present(username)==True):
            messages.error(request , "Username already exist")
            return redirect(signup_view)
        else:
            user = form.save(commit = False)
            password =  form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            new_user = authenticate(username=user.username , password=password)
            login(request , new_user)
            return redirect(index)
    return render(request,"music/signup.html",{
        "forms": NewSignUpForm
    })

def logout_view(request):
    logout(request)
    return redirect(login_view)