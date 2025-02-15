from django.contrib import admin
from .models import (
    Prueba,
)

# Register your models here.

class PruebaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripción', 'fecha_creacion', 'fecha_actualizacion',)
    search_fields = ('nombre',)

admin.site.register(Prueba, PruebaAdmin)