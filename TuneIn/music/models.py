from django.db import models

# Create your models here.
class Album(models.Model):
    album_title = models.CharField(max_length = 50)
    album_logo = models.CharField(max_length = 200)
    language = models.CharField(max_length = 100)

    def __str__(self):
        return f"{self.album_title}"