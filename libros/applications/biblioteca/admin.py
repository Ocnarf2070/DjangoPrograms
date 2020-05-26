from django.contrib import admin

# Register your models here.
from .models import *


class AutorAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'nacionalidad',
        'id'
    )
    #Atributo para buscar un campo
    search_fields = ('nombre', 'nacionalidad',)


class LibrosAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'resumen',
        'autor',
        'id'
    )
    # Atributo para buscar un campo
    search_fields = ('title',)
    # Para hace filtros
    list_filter = ('autor',)


admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibrosAdmin)