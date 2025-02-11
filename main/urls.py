from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('galeria/', views.galeria_view, name="galeria")
]