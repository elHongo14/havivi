from django.contrib import admin
from .models import (
    Prueba,
    Galeria,
    Solicitudes,
    Empleos,
    Solicitud_Empleo,
)

# Register your models here.

class PruebaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripción', 'fecha_creacion', 'fecha_actualizacion',)
    search_fields = ('nombre',)

class GaleriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripción', 'img_ubi', 'foto_bool', 'link',)
    search_fields = ('nombre', 'img_ubi')

class SolicitudesAdmin(admin.ModelAdmin):
    list_display = ('tipo','fecha','nombre','descripción','objetivo','archivo')
    search_fields = ('nombre','fecha','tipo')

class EmpleosAdmin(admin.ModelAdmin):
    list_display = ('titulo','área','descripción','requisitos','horario','paga',)
    search_fields = ('titulo','área',)

class Solicitud_EmpleoAdmin(admin.ModelAdmin):
    list_display = ('archivo','empleo',)
    search_fields = ('empleo',)

admin.site.register(Prueba, PruebaAdmin)
admin.site.register(Galeria, GaleriaAdmin)
admin.site.register(Solicitudes,SolicitudesAdmin)
admin.site.register(Empleos,EmpleosAdmin)
admin.site.register(Solicitud_Empleo,Solicitud_EmpleoAdmin)