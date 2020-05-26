from django.db import models

# Create your models here.


class Autor(models.Model):
    nombre = models.CharField('Nombres', max_length=80)
    nacionalidad = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    title = models.CharField('Titulo', max_length=150)
    resumen = models.TextField('Resumen', blank=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
