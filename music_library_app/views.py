from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from music_library_app.models import Song, Album
from .models import User


class SongList(ListView):
    model = Song


class AlbumList(ListView):
    model = Album


def login_redirect(request):
    return redirect('/profile/'+request.user.username, user_profile=request.user.username)


def user_profile(request, user_profile):
    context = {'user_profile':user_profile}
    return render(request, 'music_library_app/user.html', context)
