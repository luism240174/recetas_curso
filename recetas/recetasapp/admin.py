from django.contrib import admin

# Register your models here.


from recetasapp.models import Receta, Ingrediente, Pasos

#Receta tiene la primarykey las otras dos foreign key
class PasosInline(admin.TabularInline):
    model = Pasos
    extra =0 #por default viene con 3 

class IngredienteInline(admin.TabularInline):
    model = Ingrediente
    extra = 0
class RecetaAdmin(admin.ModelAdmin):
    inlines = [IngredienteInline, PasosInline]
    list_display = ['nombre', 'created_at']


admin.site.register(Receta, RecetaAdmin)

