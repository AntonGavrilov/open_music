from django.urls import path
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    path('login/',login,{'template_name':'authentication/login.html'}, name='login'),
    path('singup/', views.sing_up, name='register')

]