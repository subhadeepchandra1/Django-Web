from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth import login, logout
from django.contrib.auth.views import PasswordResetView,PasswordChangeDoneView

urlpatterns = [
    path('', views.home),
    path('login', auth_views.LoginView.as_view(template_name='home/login.html')),
    path('logout', auth_views.LoginView.as_view(template_name='home/logout.html')),
    path('register',views.register,name='register'),
    path('profile',views.view_profile,name='view_profile'),
    path('profile/edit',views.edit_profile,name='edit_profile'),
    path('change-password',views.change_password,name='change_password'),
    path('reset-password',PasswordResetView,name='reset_password'),
    path('reset-password/done',PasswordChangeDoneView,name='password_reset_done'),

]
