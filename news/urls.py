from django.urls import path
from . import views

app_name='news'

urlpatterns = [
    path('noticias/', views.news_view, name="noticias"),
]