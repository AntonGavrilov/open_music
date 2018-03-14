from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from music_library_app.models import Song, Album
from .models import User


class SongList(ListView):
    model = Song


class AlbumList(ListView):
    model = Album



