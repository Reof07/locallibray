from django.shortcuts import render, HttpResponse

# Create your views here.

def home_Test(request):
    return HttpResponse('hola')

