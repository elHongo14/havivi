from django.urls import path
from . import views

app_name='news'

urlpatterns = [
    path('noticias/', views.news_view, name="noticias"),
    path('noticias/n_detail/<new>', views.new_detail_view, name="n_detail"),
]