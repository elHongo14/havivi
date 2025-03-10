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

    def save_model(self, request, obj, form, change):
        if not obj.autor:
            obj.autor = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(autor=request.user)

class TipoNoticiaAdmin(admin.ModelAdmin):
    list_display = (
        'nombre_tipo',
    )
    search_fields = ('nombre_tipo',)

admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Tipo_Noticia, TipoNoticiaAdmin)