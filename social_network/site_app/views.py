from cmath import e
from multiprocessing import context
import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import NewUserForm


def registerUser(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Vartotojas sekmingai sukurtas')
            # return redirect('login') nukreips i login puslapi kai bus padarytas
    context = {'form':form}
    return render(request, 'site_app/register.html', context)

def loginUser(request):
    if request.method == 'POST':
        username =  request.POST.get('username')
        password = request.POST.get('password')

        user =  authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('')
        else:
            messages.info(request, 'Netesingas vartotojo vardas arba slaptažodis')

    context = {}
    return render(request, 'site_app/login.html', context)