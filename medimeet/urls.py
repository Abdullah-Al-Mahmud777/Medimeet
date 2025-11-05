from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('services/', include('services.urls')),
    path('about/', include('about.urls')),

]