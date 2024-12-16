from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from . forms import Registration
from django.http import HttpResponse
import re

# Create your views here.
def register(request):
    
    if(request.method=='POST'):
        fm = Registration(request.POST)
        if(fm.is_valid()):
            print(fm.cleaned_data['email'])
            print(fm.cleaned_data['password1'])
            User.objects.create_user(
                first_name = fm.cleaned_data['fname'].title(),
                last_name = fm.cleaned_data['lname'].title(),
                email = fm.cleaned_data['email'].lower(),
                username = fm.cleaned_data['email'].lower(),
                password = fm.cleaned_data['password1']
            ).save()
            return render(request, 'user/login.html', {'passError': False, 'created': True})
    else:
        fm = Registration()
    return render(request, 'user/signup.html', {'form': fm})

def login(request):
    if request.method == 'POST':
        username = request.POST['email'].lower()
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
        else:
            return render(request, 'user/login.html', {'error': True,  'created': False})
        return redirect('/')
    return render(request, 'user/login.html', {'error': False,  'create': False})

def logout(request):
    auth.logout(request)
    return render(request, 'user/login.html')

def check_user(request):
    if request.method == "GET":
        un = request.GET['usern']
        reg = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        
        if(re.fullmatch(reg, un)):
            check =  User.objects.filter(username=un)
            print(check)
            if(len(check)==1):
                return HttpResponse('User Already Exist')
            else:
                return HttpResponse("User is Valid")
        else:
            return HttpResponse("Not Valid...")
            