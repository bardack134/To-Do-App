from django.urls import reverse
from django.views.generic import View

from django.shortcuts import render, redirect

# Importamos el módulo para manejar mensajes
from django.contrib import messages

from .models import Datos

# Importamos el formulario
from .forms import DatosForm

# Create your views here.

# Creamos una vista basada en clase (VBC) llamada Registrar que hereda de View.
class Registrar(View):

    # Método GET para mostrar o crear el formulario de registro.
    def get(self, request):
        datos = Datos.objects.all()

        # Creamos una instancia del formulario personalizado.
        form = DatosForm()

        # Preparamos los datos del formulario para pasar al contexto.
        context = {
            'form': form, 
            'datos': datos,
        }

        # Mostramos en la página el formulario de registro de informacion.
        return render(request, 'home.html', context) 
    
    # Método POST para procesar los datos del formulario cuando se envía.
    def post(self, request):
        
        # Creamos una instancia del formulario con los datos del POST.
        form = DatosForm(request.POST)

        # llamamos al método de Django is_valid se utiliza para validar datos de formularios creados tanto con forms.Form como con forms.ModelForm en Django
        if form.is_valid():

             # Esto guarda los datos del formulario en la base de datos y devuelve el objeto creado
            datos=form.save()   
             
             # Mostramos un mensaje de éxito.
            messages.success(request, 'Registered successfully.') 

            #redirigimos a la misma vista de registro
            return redirect(reverse('Main:registrar'))
        
        context = {
            # Preparamos los datos del formulario (incluso si no es válido) para pasar al contexto.
            'form': form  
        }

        #Mostramos la página de registro con el formulario y posibles errores.
        return render(request, 'home.html', context)  
    

def ObtenerDatos(request):
    datos = Datos.objects.all()

 
    contexto = {
        
    }
    
 

    return render(request, 'home.html', contexto)
