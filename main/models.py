from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Prueba(models.Model):
    nombre = models.CharField(max_length=145)
    descripción = models.CharField(max_length=145, null=True, blank=True)
    fecha_creacion = models.DateTimeField(
        _('Fecha de creación'), auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(
        _('Fecha de actualización'), auto_now=True)
    class Meta:
        verbose_name = "Prueba"
        verbose_name_plural = "Pruebas"

    def __str__(self):
        return self.nombre
    
class Galeria(models.Model):
    nombre = models.CharField(max_length=205)
    descripción = models.CharField(max_length=200)
    img_ubi = models.CharField(max_length=200)
    foto_bool = models.BooleanField(default=True)
    link = models.CharField(max_length=200, default="")

class Solicitudes(models.Model):
    tipo = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add=True, auto_now=False)
    nombre = models.CharField(max_length=100)
    descripción = models.CharField(max_length=1000)
    objetivo = models.CharField(max_length=100)
    archivo = models.FileField(null=False)

class Empleos(models.Model):
    titulo = models.CharField(max_length=100)
    área = models.CharField(max_length=100)
    descripción = models.CharField(max_length=1000)
    requisitos = models.CharField(max_length=500)
    horario = models.CharField(max_length=100)
    paga = models.CharField(max_length=100)

class Solicitud_Empleo(models.Model):
    archivo = models.FileField(null=False)
    empleo = models.ForeignKey(Empleos, on_delete=models.CASCADE)
