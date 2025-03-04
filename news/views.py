from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import (
    Noticia,
    Tipo_Noticia,
)

# Create your views here.

def news_view(request):
    recent_news = Noticia.objects.all().order_by('-fecha_actualizacion')[0:10]

    context = {
        'recent_news': recent_news
    }

    return render(request, 'news.html', context)

def new_detail_view(request, new):
    this_new = Noticia.objects.get(pk=new)
    recent_news = Noticia.objects.all().order_by('-fecha_actualizacion')[0:10]

    context = {
        'this_new': this_new,
        'recent_news': recent_news,
    }

    return render(request, 'new_detail.html', context)