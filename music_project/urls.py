from main_app import views as main_views
from django.contrib import admin
from django.urls import path, include
from main_app import views as main_views

urlpatterns = [
    path('', include('main_app.urls')),
    path('admin/', admin.site.urls),
    path('authentication/', include('authentication_users.urls')),
    path('profile/', include('music_library_app.urls')),
]
