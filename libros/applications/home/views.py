from django.shortcuts import render

# Create your views here.

from django.views.generic import (
    TemplateView,
    ListView,
)


class IndexView(TemplateView):
    # Template es un archivo HTML
    template_name = "home/index.html"


class ListaLibros(ListView):
    template_name = 'home/lista.html'
    queryset = ['El quijote de la mancha', 'Codigo limpio', 'La sombrea del viento',
                'Django 3.0']
    context_object_name = 'libros'

