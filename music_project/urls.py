from django.contrib import admin
from django.urls import path, include
from music_library_app import views
from music_project import views as main_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', main_views.index),
    path('accounts/', include('django.contrib.auth.urls')),
    path('<username>/library', include('music_library_app.urls'))
]
