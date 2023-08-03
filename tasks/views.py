from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login
from django.db import IntegrityError
# Create your views here.

def home(request):
    empresa = 'Maggio'
    return render(request, 'Home.html', {'empresa': empresa})

def SignUp(request):
    if request.method == 'GET':
        print(request.POST)
        return render(request, 'SignUp.html', {
            'signup': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user) 
                return render(request, 'tasks.html')
            except IntegrityError:
                return render(request, 'tasks.html')
        else:
            return render(request, 'SignUp.html', {
                'signup': UserCreationForm, 'Error': 'Las contraseñas no coinciden'
            })
    
def login(request):
    return render(request, 'Login.html')

def tasks(request):
    return render(request, 'tasks.html')