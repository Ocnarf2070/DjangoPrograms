from django.urls import include, path, re_path
from .views import *

app_name = "biblioteca_app"

urlpatterns = [
    path('', ListaAutores.as_view(), name="lista-autores"),
    path('libros-autor/<pk>/', ListaLibroAutores.as_view(), name="lista-libros"),
    path('autor', AddAutor.as_view(), name="agnadir-autor"),
]
