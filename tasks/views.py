from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.

def SignUp(request):
    if request.method == 'GET':
        print (request.POST)
        return render(request, 'SignUp.html', {
            'signup':UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
           user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
           user.save()
           print(request.POST)
           return HttpResponse('Se creo exitosamente')
        return HttpResponse('No se creo exitosamente')