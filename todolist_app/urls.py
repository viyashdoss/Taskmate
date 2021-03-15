
from django.contrib import admin
from django.urls import path
from todolist_app import views

urlpatterns = [
    path('',views.homepage,name='homepage' ),
    path('contact/',views.contact,name='contact' ),
    path('about/',views.about,name='about' ),
    path('todolist/',views.todolist,name='todolist' ),
    path('home/',views.homepage,name='homepage')
    
]
