from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('signup/', views.SignUp, name='SignUp'),
    path('login/', views.login,name='login'),
    path('tasks', views.tasks, name='tasks')
]