from django.db import models

# Create your models here.
class Album(models.Model):
    album_title = models.CharField(max_length = 50)
    album_logo = models.ImageField()
    language = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.album_title}"

class Song(models.Model):
    album = models.ForeignKey(Album , on_delete=models.CASCADE,related_name="songs")
    song_name = models.CharField(max_length = 100)
    artist_name = models.CharField(max_length = 100)

    def __str__(self):
        return f"{self.album} : {self.song_name}"