from django.contrib import admin
from .models import (
    Noticia,
    Tipo_Noticia,
)

# Register your models here.

class NoticiaAdmin(admin.ModelAdmin):
    list_display = (
        'titular', 
        'autor', 
        'tipo_noticia', 
        'imagen_principal', 
        'fecha_creacion', 
        'fecha_actualizacion', 
        )
    search_fields = ('titular', 'autor', 'tipo_noticia',)

class TipoNoticiaAdmin(admin.ModelAdmin):
    list_display = (
        'nombre_tipo',
    )
    search_fields = ('nombre_tipo',)

admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Tipo_Noticia, TipoNoticiaAdmin)