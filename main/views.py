from django.shortcuts import render
from .models import Galeria

# Create your views here.

def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'login.html')

def galeria_view(request):
    galeria = Galeria.objects.all()
    return render(request, 'galeria.html',{
        'galeria' : galeria
    })

#test XD

# def navbar_view(request):
#     return render(request, 'navbar.html')