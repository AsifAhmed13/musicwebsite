from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,get_user_model
# Create your views here.
User = get_user_model()

class NewLoginForm(forms.Form):
    username = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(max_length=50 , widget = forms.PasswordInput(attrs={'placeholder' : 'Password'}))   
    def clean(self , *args , **kwargs):
        return super(NewLoginForm , self).clean(*args , **kwargs)

class NewSignUpForm(forms.ModelForm):
    username = forms.CharField(max_length = 50,widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(max_length = 50 , widget = forms.PasswordInput(attrs={'placeholder': 'Password'}))
    reenterpassword = forms.CharField(max_length  =50 , widget = forms.PasswordInput(attrs={'placeholder': 'Re-Enter Password'}))

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "reenterpassword"
        ]
    def clean(self, *args, **kwargs):
        return super(NewSignUpForm ,self).clean(*args , **kwargs)