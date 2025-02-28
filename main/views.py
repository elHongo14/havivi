from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Galeria
from .forms import LoginForm, solicitudForm

# Create your views here.

def home_view(request):
    user = request.user
    return render(request, 'home.html', {'user': user})

# def login_view(request):
#     return render(request, 'login.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('main:home')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            usuario = authenticate(request, username=username, password=password)
            if usuario is not None:
                auth_login(request, usuario)
                if 'next' in request.GET:
                    return redirect(request.GET['next'])
                return redirect("main:home")
            else:
                error_message = "Por favor introduzca un nombre de usuario y contraseña correctos."
                messages.error(request, error_message)
    else:
        form = LoginForm()

    context = {
        'form': form,
    }
    return render(request, 'login.html', context)


def galeria_view(request):
    galeria = Galeria.objects.all()
    return render(request, 'galeria.html',{
        'galeria' : galeria
    })

def bolsa_view(request):
    return render(request, 'bolsa_de_empleo.html')

def capacitaciones_view(request):
    return render(request, 'capacitaciones.html')

def donaciones_view(request):
    return render(request, 'donaciones.html')

def reportes_view(request):
    return render(request, 'reportes.html')

def solicitudes_view(request):
    #if request.method == 'POST':
    #    form = solicitudForm(request.POST)
    #    if form.is_valid():
    #        messages.add_message = "valido"
    #   else:
    #        messages.error = "invalido"
    context = {
        
    }
    return render(request, 'solicitudes.html',context)
#test XD

# def navbar_view(request):
#     return render(request, 'navbar.html')