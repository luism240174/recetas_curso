from django.shortcuts import render

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
            error = 'El usuario existe'
            contexto ['error'] = error

        else:
            print('Crear al usuario')



    else:
        print('GET')
        

    return render (request, 'registro/registro.html', contexto)
    