from django.shortcuts import render, redirect
from .models import Book

# Create your views here.

# Vista para crear un nuevo libro.
def create_book(request):
    # Si el método de la solicitud es POST, se crea un nuevo libro.
    if request.method == "POST":
        title = request.POST['title']
        author = request.POST['author']
        published_date = request.POST['published_date']
        # Crear y guardar el nuevo libro en la base de datos.
        Book.objects.create(title=title, author=author, published_date=published_date)
        return redirect('list_books')  # Redirigir a la lista de libros después de crear uno nuevo.
    return render(request, 'AppCRUD/create_book.html')  # Renderiza el formulario para crear un nuevo libro.

# Vista para listar todos los libros.
def list_books(request):
    # Obtener todos los libros de la base de datos.
    books = Book.objects.all()
    # Renderiza la lista de libros.
    return render(request, 'AppCRUD/list_books.html', {'books': books})

# Vista para actualizar un libro existente.
def update_book(request, id):
    # Obtener el libro por su ID.
    book = Book.objects.get(id=id)
    if request.method == "POST":
        # Actualizar los campos del libro con los datos del formulario.
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.published_date = request.POST['published_date']
        book.save()  # Guardar los cambios en la base de datos.
        return redirect('list_books')  # Redirigir a la lista de libros después de actualizar.
    return render(request, 'AppCRUD/update_book.html', {'book': book})  # Renderiza el formulario para actualizar un libro.

# Vista para eliminar un libro.
def delete_book(request, id):
    # Obtener el libro por su ID y eliminarlo.
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('list_books')  # Redirigir a la lista de libros después de eliminar uno.
