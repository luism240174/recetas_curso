from django.shortcuts import render

def registro(request):

    contexto = {}
    return render (request, 'registro/registro.html', contexto)
    