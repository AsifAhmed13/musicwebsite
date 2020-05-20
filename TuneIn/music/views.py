from .models import Album
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,get_user_model,login,logout
from .forms import UserLoginForm , UserRegistrationForm,NewAlbumForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse



def index(request):
    if(request.user.is_authenticated):
        a = User.objects.get(username=request.user.username)
        albums = a.albums.all()
        count = albums.count()
        return render(request,"music/index.html",{
            "albums": a.albums.all(),
            "user": request.user.username.capitalize(),
            "count": count
        })
    messages.error(request,"Please Login First")
    return redirect(login_view)


def login_view(request):
    if(request.user.is_authenticated):
        messages.error(request , "You were logged out")
        return redirect(logout_view)
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
    if(request.user.is_authenticated):
        messages.error(request , "You were logged out")
        return redirect(logout_view)
    if request.method=="POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password")
            reenterpassword = form.cleaned_data.get('reenterpassword')
            if password!=reenterpassword:
                messages.error(request , "Password did not match")
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

def album_exists(album_title , user):
    for album in user.albums.all():
        if(album_title==album.album_title):
            return True
    return False

def add_album(request):
    if(request.method=="POST"):
        form = NewAlbumForm(request.POST,request.FILES)
        if(form.is_valid()):
            album_title = form.cleaned_data.get('album_title')
            user = User.objects.get(username=request.user.username)
            if (album_exists(album_title ,user)==True):
                messages.error(request , "Album already exists")
                return render(request , "music/add_album.html",{
                    'forms': NewAlbumForm
                })
            a = Album()
            a.album_title = album_title
            a.language = form.cleaned_data.get('language')
            a.album_logo = request.FILES['album_logo']
            a.user = user
            a.save()      
            return redirect(index)
        else:
            return HttpResponse("Not valid")
    return render(request , "music/add_album.html",{
        'forms': NewAlbumForm
    })

def details(request,album_title):
    username = request.user.username
    user = User.objects.get(username = username)
    album = user.albums.get(album_title = album_title)
    return render(request , "music/details.html",{
        "songs" : album.songs.all(),
        "album" : album
    })

def addsong(request , album_title):
    username = request.user.username
    user = User.objects.get(username = username)
    album = user.albums.get(album_title = album_title)
    return render(request, "music/addsong.html",{
        "album": album
    })