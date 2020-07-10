from django.shortcuts import render, HttpResponse
# importa las clases de los modelos que usaremos para acceder a los datos en todas nuestras vistas.
from .models import Book, BookInstance, Author, Language, Genre

# Create your views here.

def index(request):
    """
    Función vista para la página inicio del sitio.
    """

    #Generando contadores de alguno objetos especiales.
    num_books = Book.objects.all().count
    num_instances=BookInstance.objects.all().count()
    # Libros disponibles (status = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # El 'all()' esta implícito por defecto.
   
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
        )

