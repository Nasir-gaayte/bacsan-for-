from django.shortcuts import render, redirect
from django.contrib.auth import login, logout , authenticate
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.



def home(request):
    return render(request,'bac_app/home.html')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user= form.save(commit=True)
            login(request, user)
            messages.success(request,'your in ')
            return redirect('bac_app:home')
        else:
            messages.error(request,'something gos wrong')
    form = RegisterForm()            
    return render(request,'bac_app/register.html',{
        'register_form':form,
        'messages':messages,
    })


def login_requeset(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username= username, password= password)
            if user is not None:
                login(request, user)
                messages.success(request,f'wellcome{username}')
                return redirect ('bac_app:home')
            else:
                messages.info(request,'something gos wrong')
    form = AuthenticationForm()            
    return render(request,'bac_app/login.html',{
        'login_form': form,
    })



def logout_request(request):
    logout(request)
    return redirect('bac_app:home')