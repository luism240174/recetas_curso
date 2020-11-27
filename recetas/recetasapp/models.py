from django.db import models
from django.contrib.auth.models import User

class Receta(models.Model):
    nombre = models.CharField(max_length=200)
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Ingrediente(models.Model):
    UNIDADES = [
        ('unidades', 'Unidades'),
        ('litros', 'Litros'),
        ('cucharadas', 'Cucharadas'),
        ('gramos', 'Gramos'),
        ('kilos','Kilos'),
    ]

    nombre = models.CharField(max_length=200)
    cantidad  = models.IntegerField(default=1)
    unidad = models.CharField(max_length = 20, choices=UNIDADES, default='unidades')
    receta = models.ForeignKey(Receta, related_name ='ingredientes', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    
class Pasos(models.Model):

    numero = models.IntegerField(default=1)
    explicacion = models.TextField()
    receta = models.ForeignKey(Receta, related_name ='pasos', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)




    


