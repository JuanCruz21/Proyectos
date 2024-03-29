from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.SignUp, name='SignUp'),
    path('Signin/', views.Signin, name='Signin'),
    path('logout/', views.signout,name='logout'),
    path('tasks/', views.tasks, name='tasks'),
    path('taskComplete/', views.tasks_complete, name='taskscomplete'),
    path('NewTask/', views.Newtasks , name='NewTask'),
    path('task/<int:task_id>', views.DetailTask, name='taskdetail'),
    path('task/<int:task_id>/complete', views.TaskComplete, name='taskcomplete'),
    path('task/<int:task_id>/delete', views.TaskDelete, name='taskdelete')
]