from .models import Album,logo_default,Song
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,get_user_model,login,logout
from .forms import UserLoginForm , UserRegistrationForm,NewAlbumForm,NewSongForm,SearchForm
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
            if "album_logo" in request.FILES:
                a.album_logo = request.FILES["album_logo"]
            else:
                d = logo_default()
                a.album_logo = d["logo"]
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

def song_exists(song_name , album):
    for song in album.songs.all():
        if(song.song_name==song_name):
            return True
    return False

def addsong(request , album_title):
    if(request.method=="POST"):
        form = NewSongForm(request.POST,request.FILES)
        if(form.is_valid()):
            user = User.objects.get(username=request.user.username)
            albums = user.albums.all()
            album  = albums.get(album_title=album_title)
            song_name = form.cleaned_data.get('song_name')
            if(song_exists(song_name,album)==True):
                messages.error(request,"Song already exists in this album")
                return render(request,"music/addsong.html",{
                    "album": album,
                    "forms": NewSongForm
                })
            song = Song()
            song.album = album
            song.song_name = song_name
            song.artist_name = form.cleaned_data.get('artist_name')
            song.audio_file = request.FILES["audio_file"]
            song.save()
            return redirect(details,album_title)
    username = request.user.username
    user = User.objects.get(username = username)
    album = user.albums.get(album_title = album_title)
    return render(request, "music/addsong.html",{
        "album": album,
        "forms": NewSongForm
    })

def mysongs(request):
    user = User.objects.get(username = request.user.username)
    albums = user.albums.all()
    count = albums.count()
    flag = 0
    songcount =1 
    for album in albums:
        if(album.songs.all().count()!=0):
            flag = 1
            break
    if(flag==0 and count!=0):
        songcount = 0
    return render(request,"music/mysongs.html",{
        "albums": albums,
        "user": request.user.username.capitalize(),
        "count": count,
        "songcount": songcount
    })

def deletealbum(request,album_title):
    user = User.objects.get(username = request.user.username)
    albums = user.albums.all()
    albums = albums.filter(album_title =album_title).delete()
    albums = user.albums.all()
    return redirect(index)

def deletesong(request ,album_title, song_name):
    user = User.objects.get(username = request.user.username)
    albums = user.albums.all()
    album = albums.get(album_title = album_title)
    songs = album.songs.all()
    songs = songs.filter(song_name = song_name).delete()
    songs  = album.songs.all()
    return redirect(details,album_title)

def playsong(request,album_title , song_name):
    user = User.objects.get(username=request.user.username)
    albums = user.albums.all()
    album = albums.get(album_title = album_title)
    song = album.songs.get(song_name = song_name)
    return render(request,"music/playsong.html",{
        "song": song
    })

def playsongs(request , album_title,song_name):
    user = User.objects.get(username=request.user.username)
    albums = user.albums.all()
    album = albums.get(album_title = album_title)
    song = album.songs.get(song_name = song_name)
    return render(request,"music/playsongs.html",{
        "song": song
    })



def search(request):
    if request.method=="POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            q = form.cleaned_data.get('q')
            user = User.objects.get(username=request.user.username)
            albums = user.albums.all()
            sendalbums = []
            songslist = []
            sendsongs = []
            for album in albums:
                songslist.append(album.songs.all())
                if(q in album.album_title or q.capitalize() in album.album_title):
                    sendalbums.append(album)
            for songs in songslist:
                for song in songs:
                    if(q in song.song_name or q.capitalize() in song.song_name):
                        sendsongs.append(song)
            if(len(sendalbums)==0 and len(sendsongs)==0):
                messages.error(request,"NO ALBUMS FOUND")
                return render(request , "music/search.html",{
                    "count" : 0
                } )
            return render(request , "music/search.html",{
                "songslist": sendsongs,
                "albumslist": sendalbums,
                "user": request.user.username.capitalize(),
                "count": 1
            })
        return redirect(index)
    return redirect(index)

def playsearch(request,album_title,song_name):
    user = User.objects.get(username=request.user.username)
    albums = user.albums.all()
    album = albums.get(album_title = album_title)
    song = album.songs.get(song_name = song_name)
    return render(request,"music/playsearch.html",{
        "song": song
    })

def searchdetails(request,album_title):
    return redirect(details,album_title)