from django.http import HttpResponse
from django.shortcuts import render


def home(request):

    #return HttpResponse('<h1>Hello World</h1>')
    contexto = {}
    return render(request,'home.html', contexto)

def contacto(request):

    contexto = {}
    return render (request,'contacto.html', contexto)

