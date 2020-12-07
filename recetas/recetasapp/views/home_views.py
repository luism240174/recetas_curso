from django.http import HttpResponse
from django.shortcuts import render
from recetasapp.models import Receta
from django.core.mail import send_mail

def home(request):

    #return HttpResponse('<h1>Hello World</h1>')
    recetas = Receta.objects.all()

    contexto = {
        'recetas' : recetas
    }

    return render(request,'home.html', contexto)

def contacto(request):

    contexto = {}
    if request.method == 'POST':
        print('Enviar email')

        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')  

        #print('{} {}'.format(email, mensaje))
        mensaje_html = 'email {} <br> mensaje: {}'.format(email, mensaje)
        send_mail("Contacto de recetas", mensaje_html,
                    'info@recetas.com',['destinatario@recetas.com'])

        contexto ['mensaje'] = 'Petición enviada correctamente'
    return render (request,'contacto.html', contexto)

