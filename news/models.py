from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

import datetime

from django.contrib.auth.models import User

# Create your models here.

class Tipo_Noticia(models.Model):
    nombre_tipo = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Tipo de Noticia"
        verbose_name_plural = "Tipos de Noticia"

    def __str__(self):
        return self.nombre_tipo

class Noticia(models.Model):
    titular = models.CharField(max_length=200)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, editable=False)
    cuerpo_noticia = RichTextField(_('Cuerpo Noticia'), null=True, blank=True)
    tipo_noticia = models.ForeignKey(Tipo_Noticia, on_delete=models.CASCADE, null=True, blank=True)
    imagen_principal = models.ImageField(
        default='dummy_img.jpg', upload_to='noticias', help_text="El tamaño de la imagen deberá ser menor a 2MB", blank=True, null=True)
    fecha_creacion = models.DateTimeField(
        _('Fecha de creación'), auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(
        _('Fecha de actualización'), auto_now=True)
    
    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"

    def __str__(self):
        return self.titular