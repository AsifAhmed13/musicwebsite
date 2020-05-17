from django.shortcuts import render
from .models import Album
# Create your views here.
def index(request):
    return render(request,"music/index.html",{
        "albums": Album.objects.all(),
    })