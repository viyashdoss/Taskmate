from django.shortcuts import render,redirect
from django.http import HttpResponse
from  todolist_app.models import Tasklist
from todolist_app.form import Taskform





# Create your views here.
def homepage(request):
    
    return render(request,'home.html',{'content':'it is homepage'})

def todolist(request):
    task_obj = Tasklist.objects.all()  
    return render(request,'todolist.html',{'content':task_obj})


def about(request):
    
    return render(request,'about.html',{'content':'it is about page'})


def contact(request):
    
    return render(request,'contact.html',{'content':'it is contact page'})


