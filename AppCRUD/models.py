from django.db import models

# Create your models here.

# Modelo Book: representa un libro en la base de datos.
class Book(models.Model):
    # Título del libro, limitado a 200 caracteres.
    title = models.CharField(max_length=200)
    # Autor del libro, limitado a 100 caracteres.
    author = models.CharField(max_length=100)
    # Fecha de publicación del libro.
    published_date = models.DateField()
    