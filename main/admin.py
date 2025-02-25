from django.contrib import admin
from .models import (
    Prueba,
    Galeria,
)

# Register your models here.

class PruebaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripción', 'fecha_creacion', 'fecha_actualizacion',)
    search_fields = ('nombre',)

class GaleriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripción', 'img_ubi', 'foto_bool', 'link',)
    search_fields = ('nombre', 'img_ubi')

admin.site.register(Prueba, PruebaAdmin)
admin.site.register(Galeria, GaleriaAdmin)