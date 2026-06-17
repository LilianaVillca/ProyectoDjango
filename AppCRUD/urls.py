from django.urls import path
from . import views

# Definir las rutas y las vistas correspondientes.
urlpatterns = [
    path('crear', views.create_book, name='create_book'),  # URL para crear un nuevo libro.
    path('', views.list_books, name='list_books'),  # URL para listar todos los libros.
    path('actualizar/<int:id>/', views.update_book, name='update_book'),  # URL para actualizar un libro existente.
    path('eliminar/<int:id>/', views.delete_book, name='delete_book'),  # URL para eliminar un libro.
]
