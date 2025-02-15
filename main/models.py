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