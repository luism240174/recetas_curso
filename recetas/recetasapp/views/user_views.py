from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.urls import reverse


def registro(request):

    contexto = {}

    if request.method == 'POST':
        print('POST')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_exist = User.objects.filter(username = username).exists() #Return True or False
        if user_exist:
            error = 'El nombre de usuario ya existe'
            contexto ['nombre'] = nombre
            contexto ['apellido'] = apellido
            contexto ['username'] = username
            contexto ['email'] = email
            
            
            

        else:
            print('Crear al usuario')
            User.objects.create_user(username, email, password, first_name=nombre, last_name=apellido)
            url = "{}?greetings=true".format(reverse('login'))
            return redirect(url)           
            

    else:
        print('GET')
        

    return render (request, 'usuario/registro.html', contexto)
    
def login(request):

    contexto = {}
    if request.method == 'GET':
        greetings = request.GET.get('greetings')
        print('greetings: {}'.format(greetings))
        if greetings == "true":
            contexto ['mensaje'] = 'Cuenta creada correctamente, por favor autentícate'
        
    else:
        usename = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            auth_login (request, user)
            return redirect(reverse('home'))
        else:
            contexto ['error'] = 'Error al autenticar'


    return render (request, 'usuario/login.html', contexto)

