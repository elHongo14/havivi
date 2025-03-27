from django.urls import path
from . import views

app_name='main'

urlpatterns = [
    path('', views.home_view, name="home"),
    path('login/', views.login_view, name="login"),
    path('galeria/', views.galeria_view, name="galeria"),
    path('empleo/', views.bolsa_view, name="empleo"),
    path('donaciones/', views.donaciones_view, name="donaciones"),
    path('descargas/', views.descargas_view, name="descargas"),
    path('solicitudes/', views.solicitudes_view, name="solicitudes"),
    # path('navbar/', views.navbar_view, name="navbar"),
]