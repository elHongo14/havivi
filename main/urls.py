from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('login/', views.login_view, name="login"),
    path('galeria/', views.galeria_view, name="galeria"),
    # path('navbar/', views.navbar_view, name="navbar"),
]