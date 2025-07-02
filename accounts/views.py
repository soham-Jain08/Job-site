import time
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *


# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        email = request.POST.get('email')
        dateofbirth = request.POST.get('dob')

        if not User.objects.filter(username=username).exists():
            user = User.objects.create(username=username, password=password, email=email)
            CustomUser.objects.create(user=user, dateofbirth=dateofbirth)
            return redirect('login')
        else:
            messages.error(request, 'Username already exists, please go to login page')

    return render(request, 'accounts/signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Username does not exist')
            return redirect('/accounts/login')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def build_profile(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        bio = request.POST.get('bio')
        

        UserProfile.objects.create(
            user=request.user,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            bio=bio
        )
        
        return redirect('')

    return render(request, 'accounts/profile.html')
