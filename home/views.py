from django.shortcuts import render,HttpResponse,redirect
#from django.contrib.auth.forms import UserCreationForm
from home.forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

# Create your views here.
def home(request):
    return render(request,'home/index.html')

def register(request):
    if request.method == 'POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')

    form=RegistrationForm()
    args={'form':form}
    return render(request,'home/reg_form.html',args)

def view_profile(request):
    args={'user':request.user}
    return render(request,'home/profile.html',args)

def edit_profile(request):
    if request.method=='POST':
        form=UserChangeForm(request.POST,instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('home/profile')

    else:
        form=UserChangeForm(instance=request.user)
        args={'form':form}
        return render(request,'home/edit_profile.html',args)
