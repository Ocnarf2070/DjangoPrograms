from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
)

from .models import *


class ListaAutores(ListView):
    template_name = 'biblioteca/lista_autores.html'
    model = Autor
    context_object_name = 'autores'

class ListaLibroAutores(ListView):
    """
        Vista para listar libros por autor
    """
    template_name = 'biblioteca/lista_libros.html'
    model = Libro
    context_object_name = 'libros'

    def get_queryset(self):
        # Identificar el usuario
        id = self.kwargs['pk']
        # Filtro de los libros
        lista = Libro.objects.filter(autor=id)
        # Devuelvo la lista
        return lista

class AddAutor(CreateView):
    """
        Vista para registrar un nuevo autor
    """
    template_name = "biblioteca/add_autor.html"
    model = Autor
    fields = ['nombre', 'nacionalidad']
    success_url = '/'
