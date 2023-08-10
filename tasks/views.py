from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from .forms import TaskForm
from .models import Task
from django.utils import timezone
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
    
def Signin(request):
    if request.method == 'GET':
        return render(request, 'Signin.html', {
            'signin': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST
            ['password'])
        if user is None:
            return render(request, 'Signin.html', {
                'signin': AuthenticationForm, 
                'Error' :'Usuario no existe o contraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect('tasks')

def tasks(request):
    Tareas = Task.objects.filter(user=request.user, datecomplete__isnull=True)
    return render(request, 'tasks.html', {'tasks':Tareas})

def tasks_complete(request):
    Tareas = Task.objects.filter(user=request.user, 
                datecomplete__isnull=False).order_by('-datecomplete')
    return render(request, 'tasks.html', {'tasks':Tareas})

def Newtasks(request):
    if request.method == 'GET':
        return render(request, 'CreateTask.html', { 'form': TaskForm })
    else:
        Newtask = TaskForm(request.POST)
        new_task = Newtask.save(commit=False)
        new_task.user = request.user
        new_task.save()
        return redirect('tasks')
    
def DetailTask(request,task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task,pk=task_id)
        form = TaskForm(instance=task)
        return render(request, 'taskdetail.html', {'task':task,'form': form})
    else:
        try:
            task = get_object_or_404(Task,pk=task_id, user=request.user)
            form = TaskForm(request.POST,instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'taskdetail.html', {'task':task,'form': form,'Error': "No se pudo actualizar"})

def signout(request):
    logout(request)
    return redirect('home')

def TaskComplete(request,task_id):
    task = get_object_or_404(Task,pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecomplete = timezone.now()
        task.save()
        return redirect('taskscomplete')
    
def TaskDelete(request,task_id):
    task = get_object_or_404(Task,pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')