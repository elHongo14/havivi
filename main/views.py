from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Galeria, Solicitudes, Empleos, Solicitud_Empleo, Descargas
from .forms import LoginForm, solicitudForm, solicitud_Empleo_Form

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
    pagina = request.GET.get("page",1)
    try:
        paginación = Paginator(galeria, 45)
        galeria = paginación.page(pagina)
    except:
        paginación = Paginator(galeria, 45)
        galeria = paginación.page(1)
        messages.info(request,"La página que intentas buscar no existe.")
    return render(request, 'galeria.html',{
        'objeto' : galeria,
        "paginación": paginación
    })

def bolsa_view(request):
    empleos = Empleos.objects.all()
    pagina = request.GET.get("page",1)
    try:
        paginación = Paginator(empleos, 15)
        empleos = paginación.page(pagina)
    except:
        paginación = Paginator(empleos, 15)
        empleos = paginación.page(1)
        messages.info(request,"La página que intentas buscar no existe.")
    if request.method == 'GET':
        form = solicitud_Empleo_Form()
    if request.method == 'POST':
        form = solicitud_Empleo_Form(request.POST, request.FILES)
        file = request.FILES['archivo_curriculum']
        if form.is_valid():
            curriculum = Solicitud_Empleo.objects.create(
                archivo = file,
                empleo = Empleos.objects.get(id = form.cleaned_data['id_empleo'])
            )
            curriculum.save()
            print(file)
            print(empleos[int(form.cleaned_data['id_empleo'])-1].titulo)
            messages.success(request, "¡Curriculum enviado con exito para "+ empleos[int(form.cleaned_data['id_empleo'])-1].titulo +"!")
        else:
            print("invalido")
            form = solicitud_Empleo_Form()
    return render(request, 'bolsa_de_empleo.html',{
        'objeto' : empleos,
        'paginación': paginación,
        'form':form,
    })

def donaciones_view(request):
    return render(request, 'donaciones.html')

def descargas_view(request):
    descargas = Descargas.objects.all()
    pagina = request.GET.get("page",1)
    try:
        paginación = Paginator(descargas, 30)
        descargas = paginación.page(pagina)
    except:
        paginación = Paginator(descargas, 30)
        descargas = paginación.page(1)
        messages.info(request,"La página que intentas buscar no existe.")
    return render(request, 'descargas.html',{
        'objeto' : descargas,
        'paginación': paginación,
    })

def solicitudes_view(request):
    context = {
        'form' : solicitudForm()
    }
    print(request.user)
    if request.method == 'POST':
        form = solicitudForm(request.POST, request.FILES)
        file = request.FILES['archivo_solicitud']
        if form.is_valid():
            #print(request.user)
            solicitud = Solicitudes.objects.create(
                tipo=form.cleaned_data['tipo_solicitud'],
                nombre=form.cleaned_data['titulo_solicitud'],
                descripción=form.cleaned_data['descripcion_solicitud'],
                objetivo=form.cleaned_data['objetivo_solicitud'],
                archivo=file
            )
            solicitud.save()
            messages.success(request, "¡Solicitud enviada con exito!")
        else:
            context = {'form' : form}
            messages.error(request, "La solicitud no fue enviada, completa todos los campos.")
            return render(request, 'solicitudes.html',context)
    
    return render(request, 'solicitudes.html',context)

#test XD

# def navbar_view(request):
#     return render(request, 'navbar.html')