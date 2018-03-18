from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'music_library_app'

urlpatterns = [
    path('<str:user_profile>',views.user_profile),
    path('library/songs/', views.SongList.as_view(),name='songs'),
    path('library/albums/', views.AlbumList.as_view(),name='albums'),
    path('login_redirect/', views.login_redirect),
    # path('playlists/',)
]