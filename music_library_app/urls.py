from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'music_library_app'

urlpatterns = [
    # path('',views.IndexUser),
    path('songs/', views.SongList.as_view(),name='songs'),
    path('albums/', views.AlbumList.as_view(),name='albums'),
    # path('artists/',),
    # path('playlists/',)
]