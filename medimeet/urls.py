# medimeet/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome, you are logged in!</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('', home, name='home'),
]
