from .models import Album
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,get_user_model,login,logout
from .forms import UserLoginForm , UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse


def index(request):
    return render(request,"music/index.html",{
        "albums": Album.objects.all(),
    })


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
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
            login(request , user)
        return redirect(index)
    return render(request, "music/login.html",{
        'forms': UserLoginForm
    })


def signup_view(request):
    if request.method=="POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password")
            reenterpassword = form.cleaned_data.get('reenterpassword')
            username = form.cleaned_data.get('username')
            if password!=reenterpassword:
                messages.error(request , "Password did not match")
                return render(request , "music/signup.html",{
                "forms": form
            })      
            a = User.objects.filter(username=username).first()
            if(a!=None):
                messages.error(request,"Username already exits")
                return render(request , "music/signup.html",{
                "forms": form
            })
            user.set_password(password)
            user.save()
            new_user = authenticate(username=user.username,password=password)
            login(request,new_user)
            return redirect(index)
        else:
            messages.error(request,"Username Already Exists")
            return render(request , "music/signup.html",{
                "forms": form
            })
    return render(request, "music/signup.html",{
        'forms': UserRegistrationForm
    })

def logout_view(request):
    logout(request)
    return redirect(login_view) 
