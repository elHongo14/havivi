from django.urls import path
from . import views

app_name='main'

urlpatterns = [
    path('', views.home_view, name="home"),
    path('login/', views.login_view, name="login"),
    path('galeria/', views.galeria_view, name="galeria"),
    path('empleo/', views.bolsa_view, name="empleo"),
    path('capacitaciones/', views.capacitaciones_view, name="capacitaciones"),
    path('donaciones/', views.donaciones_view, name="donaciones"),
    path('reportes/', views.reportes_view, name="reportes"),
    path('solicitudes/', views.solicitudes_view, name="solicitudes"),

    # path('navbar/', views.navbar_view, name="navbar"),
]