from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
import uuid # Requerida para las instancias de libros únicos


# Create your models here.

class Genre(models.Model):
    '''
    Modelo que representa un género literario (p. ej. ciencia ficción, poesía, etc.). 
    '''
    name = models.CharField(
    max_length=200, 
    help_text= 'Ingrese el nombre del género (p. ej. Ciencia Ficción, Poesía Francesa etc.)'
    )

    def __str__(self):
        '''
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
        '''
        return self.name

class Language(models.Model):
    '''
    Model representing a Language (e.g. English, French, Japanese, etc.)
    '''

    name = models.CharField(
        max_length = 100,
        help_text = 'Enter the books natural language (e.g. English, French, Japanese etc.)'
    )

    def __str__(self):
        '''String for representing the Model object (in Admin site etc.)'''
        return self.name

class Book (models.Model):
    '''
    Modelo que representa un libro (pero no un Ejemplar específico).
    '''
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True
        )
    # ForeignKey, ya que un libro tiene un solo autor, pero el mismo autor puede haber escrito muchos libros.
    # 'Author' es un string, en vez de un objeto, porque la clase Author aún no ha sido declarada.
    
    summary = models.TextField(
        max_length=1000, 
        help_text= 'Ingrese una breve descripción del libro'
        )
    
    isbn = models.CharField(
        'ISBN', 
        max_length=13, 
        help_text='13 Caracteres <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>'
        )
    
    genre = models.ManyToManyField(Genre, help_text='Seleccione un genero para este libro')
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    objects = models.Manager() # deshacerse de esa advertencia Vsc class has not object
    
    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        Esto se debe a que no podemos mostrar la infomacion de genre, es una relacion
        muchos a muchos, esto tendria un alto costo a la base de datos.
        """
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ]) # pylint: disable=E1101

    
    display_genre.short_description = 'Genre'    

    def __str__(self):
        '''
        String que representa al objeto Book
        '''
        return self.title

    def  get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Book,
        Nota: esto permite en la pagina admin que al hacer clik en el
        nombre del libro podamos ir a sus detalles y editar
        """   
        return reverse('book-detail', args=[str(self.id)]) # pylint: disable=E1101

class BookInstance(models.Model):
    '''
    Modelo que representa una copia específica de un libro (i.e. que puede ser prestado por la biblioteca).
    '''
    id = models.UUIDField(
        primary_key = True, 
        default=uuid.uuid4, 
        help_text='ID único para este libro particular en toda la biblioteca'
        ) 
    
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=2000)
    due_back = models.DateField(null=True, blank=True)
   # borrower = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True)
    objects = models.Manager()

    #
    LOAN_STATUS = (
        ('m','Maintenance'),
        ('o','On loan'),
        ('a', 'Available'),
        ('r','Reserved'),
    )

    status = models.CharField(
        max_length=1, 
        choices=LOAN_STATUS, 
        blank=True, 
        default='m', 
        help_text='Disponibilidad del libro'
        )
    
    class Meta:
        ordering = ['due_back']



    def __str__(self):
        '''
        String para representar el Objeto del Modelo
        '''
        return '{0} ({1})'.format(self.id, self.book.__str__())


class Author(models.Model):
    '''
    Modelo que representa un autor
    '''
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    objects = models.Manager()
    def get_absolute_url(self):
        '''
         Retorna la url para acceder a una instancia particular de un autor.
        '''
        return reverse('author-detail', args=[str(self.id)]) # pylint: disable=E1101

    def __str__(self):
        return '{0} ({1})' .format(self.last_name, self.first_name)


