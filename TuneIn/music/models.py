from django.db import models
from django.contrib.auth.models import User
# Create your models here.


def logo_default():
    return {"logo": 'default.png'}

class Album(models.Model):
    user =  models.ForeignKey(User , on_delete = models.CASCADE,related_name="albums",null=True,blank=True)
    album_title = models.CharField(max_length = 50)
    album_logo = models.ImageField(null=True,blank=True,default=logo_default)
    language = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.album_title}"

    
class Song(models.Model):
    album = models.ForeignKey(Album , on_delete=models.CASCADE,related_name="songs",null=True,blank=True)
    song_name = models.CharField(max_length = 100)
    artist_name = models.CharField(max_length = 100)
    audio_file = models.FileField(null=True)

    def __str__(self):
        return f"{self.album} : {self.song_name}"