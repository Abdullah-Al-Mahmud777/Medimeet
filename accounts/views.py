# accounts/views.py
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # redirect after successful login
        else:
            context = {'error': 'ইমেইল বা পাসওয়ার্ড ভুল'}
            return render(request, 'accounts/login.html', context)
    return render(request, 'accounts/login.html')
