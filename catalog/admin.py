from django.contrib import admin
from .models import  Genre

# Register your models here.
    

# registramos nuestro modeloo genero al panel admin
admin.site.register(Genre)