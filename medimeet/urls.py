from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Medimeet!")

urlpatterns = [
    path('', home, name='home'),  # <-- এটা নতুন যোগ
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]