from django.urls import include, path, re_path
from .views import *

app_name = "home_app"

urlpatterns = [
    path('index', IndexView.as_view(), name="index"),
    path('libros', ListaLibros.as_view(), name="lista")
]
