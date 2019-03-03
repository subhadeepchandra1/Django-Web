from django.shortcuts import render,HttpResponse,redirect
#from django.contrib.auth.forms import UserCreationForm
from home.forms import (
    RegistrationForm,
    EditProfileForm
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'home/index.html')

def register(request):
    if request.method == 'POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('/home')

    form=RegistrationForm()
    args={'form':form}
    return render(request,'home/reg_form.html',args)

def view_profile(request):
    args={'user':request.user}
    return render(request,'home/profile.html',args)

def edit_profile(request):
    if request.method=='POST':
        form=EditProfileForm(request.POST,instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('home/profile')

    else:
        form=EditProfileForm()
        args={'form':form}
        return render(request,'home/edit_profile.html',args)

@login_required
def change_password(request):
    if request.method=='POST':
        form=PasswordChangeForm(data=request.POST,user=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')

        else:
            return redirect('change-password')

    else:
        form=PasswordChangeForm(user=request.user)
        args={'form':form}
        return render(request,'home/change_password.html',args)
