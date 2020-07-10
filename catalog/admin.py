from django.contrib import admin
from .models import  Genre, Book, BookInstance, Language, Author

# Register your models here.

# A la hora de hacer post:
''' Edición en cadena de registros asociado,
agregar registros asociados al mismo tiempo
obteniendo inf tanto del autor como del libro.

Creamos una clase que hace uso de StackedInline
para diseño horiazotal o  StackedInline para vertical

Puedes añadir la información de Book dentro de nuestro detalle de Author
añadiendo en la clase AuthorAdmin inline= [bookInline]
'''   
class BooksInline(admin. StackedInline):
    model = Book   #modelo associado.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    '''
    PARA FORMULARIOS
    El atributo fields lista solo los campos que se van a desplegar en el formulario, en orden.
    Los campos se despliegan en vertical por defecto, pero se desplegarán en horizontal
     si los agrupas en una tupla
    '''
    inlines = [BooksInline] # agrega la informacion del modelo associado.
 
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','display_genre')
    inlines = [BooksInstanceInline]

# Register the Admin classes for BookInstance using the decorator

@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    '''
    PARA FORMULARIOS
    Puedes añadir "secciones" para agrupar información relacionada del modelo
     dentro del formulario de detalle, usando el atributo fieldsets.
    '''
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

    '''
    Cada sección tiene su propio título (o None, si no quieres un título)
    y una tupla de campos asociada en un diccionario -- el formato es complicado
    de describir pero bastante fácil de entender si observas el fragmento de código
    que se encuentra justo arriba.
    '''

# registramos el admin class con nuestro modelos associados. 
admin.site.register(Genre)
#admin.site.register(Book)
#admin.site.register(BookInstance)
admin.site.register(Language)
admin.site.register(Author,AuthorAdmin)