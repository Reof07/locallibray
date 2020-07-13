from django.shortcuts import render, HttpResponse, Http404
# importa las clases de los modelos que usaremos para acceder a los datos en todas nuestras vistas.
from .models import Book, BookInstance, Author, Language, Genre

# importar clase de vistas genericas.
from  django.views import generic

# Create your views here.

def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    """
    obtener el numero de veces que se visita la pagina
    """
    # Number of visits to this view, as counted in the session variable.
    num_visits= request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    #Generando contadores de alguno objetos especiales.
    num_books = Book.objects.all().count
    num_instances=BookInstance.objects.all().count()
    # Libros disponibles (status = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # El 'all()' esta implícito por defecto.
   
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors, 'num_visits':num_visits},
        )

class BookListView(generic.ListView):
    '''
    esta clase crea una vista generica basada en clase,
    para esto resive como parametro la clase vista de listas
    '''
    model = Book 
    paginate_by = 2


#OJO: con esta clase me da un error a la hora de pasar le id por url
class BookDetailView(generic.DetailView):
    model= BookInstance 


def book_detail_view(request,pk):
    try:
        book_id=Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")

    #book_id=get_object_or_404(Book, pk=pk)
    
    return render(
        request,
        'catalog/book_detail.html',
        context={'book':book_id,}
    )

class Authorlist(generic.ListView):
    model = Author


def author_detail_view(request,pk):
    try:
        author_id=Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        raise Http404("Author does not exist")

    #book_id=get_object_or_404(Book, pk=pk)
    
    return render(
        request,
        'catalog/author_detail.html',
        context={'author':author_id,}
    )    