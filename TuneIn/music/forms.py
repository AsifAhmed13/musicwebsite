from django import forms
from django.contrib.auth import authenticate,get_user_model
from .models import Album,Song

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder': 'Password'}))

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    reenterpassword = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Re-Enter Password'}))

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'reenterpassword',
        ]

class NewAlbumForm(forms.ModelForm):
    album_title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Album Title'}))
    language = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Language'}))

    class Meta:
        model = Album
        fields = [
            'album_title',
            'language',
            'album_logo'
        ]

class NewSongForm(forms.ModelForm):
    song_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Song Name'}))
    artist_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Artist Name'}))

    class Meta:
        model = Song
        fields = [
            'song_name',
            'artist_name',
            'audio_file'
        ]

class SearchForm(forms.Form):
    q = forms.CharField()