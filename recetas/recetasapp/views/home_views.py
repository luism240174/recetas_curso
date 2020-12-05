from django.http import HttpResponse
from django.shortcuts import render
from recetasapp.models import Receta


def home(request):

    #return HttpResponse('<h1>Hello World</h1>')
    recetas = Receta.objects.all()

    contexto = {
        'recetas' : recetas
    }

    return render(request,'home.html', contexto)

def contacto(request):

    contexto = {}
    return render (request,'contacto.html', contexto)

