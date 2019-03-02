from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request,'home/index.html')

def register(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form=UserCreationForm()
        args={'form':form}
        return render(request,'home/reg_form.html',args)
