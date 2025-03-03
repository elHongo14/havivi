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
    recent_news = Noticia.objects.all()[0:10]

    context = {
        'recent_news': recent_news
    }

    return render(request, 'news.html', context)