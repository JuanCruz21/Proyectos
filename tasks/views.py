from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
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
                return render(request, 'SignUp.html', {
                'signup': UserCreationForm, 'Error': 'Usuario ya existe'
            })
        else:
            return render(request, 'SignUp.html', {
                'signup': UserCreationForm, 'Error': 'Las contraseñas no coinciden'
            })
    
def log(request):
    if request.method == 'GET':
        return render(request, 'Login.html', {
            'signin': AuthenticationForm
        })
    else:
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request, 'Login.html', {
                'signin': AuthenticationForm, 'Error' :'Usuario no existe'
        })
        else:
            login(request, user)
            return redirect('tasks')

def tasks(request):
    return render(request, 'tasks.html')

def signout(request):
    logout(request)
    return redirect('home')