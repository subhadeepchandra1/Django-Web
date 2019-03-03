from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home),
    path('login', auth_views.LoginView.as_view(template_name='home/login.html')),
    path('logout', auth_views.LoginView.as_view(template_name='home/logout.html')),
    path('register',views.register,name='register'),
    path('profile',views.profile,name='profile'),
]
