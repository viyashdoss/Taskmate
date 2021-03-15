
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('todolist_app.urls')),
    path('contact/',include('todolist_app.urls')),
    path('about/',include('todolist_app.urls')),
    path('todolist/',include('todolist_app.urls')),
    path('home/',include('todolist_app.urls')),
]
