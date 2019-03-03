from django.shortcuts import render,HttpResponse,redirect
#from django.contrib.auth.forms import UserCreationForm
from home.forms import RegistrationForm
from django.contrib.auth.models import User

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

def profile(request):
    args={'user':request.user}
    return render(request,'home/profile.html',args)
