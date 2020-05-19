from django import forms
from django.contrib.auth import authenticate,get_user_model
from .models import Album

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

    class Meta:
        model = Album
        fields = [
            'album_title',
            'language',
            'album_logo'
        ]