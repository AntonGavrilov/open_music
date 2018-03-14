from django.db import models
from django.contrib.auth.models import User


class Artist(models.Model):
    name = models.CharField(max_length=256)
    country = models.CharField(max_length=128)
    City = models.CharField(max_length=128)
    Bio = models.TextField()

    def __str__(self):
        return self.name


class Gener(models.Model):
    name = models.CharField(max_length=128)
    artists = models.ManyToManyField(Artist)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=128)
    year = models.DateField()

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=128)
    artist = models.ForeignKey(Artist, related_name='of_the_group', on_delete=models.CASCADE)
    album = models.ForeignKey(Album, related_name='album', on_delete=models.CASCADE)
    last_play = models.DateTimeField(auto_now=True)
    file_path = models.TextField(blank=True)



    def __str__(self):
        return self.name

class Playlist(models.Model):
    user = models.ManyToManyField(User)
    name = models.CharField(max_length=128)
    songs = models.ManyToManyField('Song', related_name='songs', blank=True)

    def __str__(self):
        return self.name
