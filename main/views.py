from django.views.generic import View

from django.shortcuts import render

# Importamos el módulo para manejar mensajes
from django.contrib import messages

# Importamos el formulario
from .forms import DatosForm

# Create your views here.

# Creamos una vista basada en clase (VBC) llamada Registrar que hereda de View.
class Registrar(View):

    # Método GET para mostrar o crear el formulario de registro.
    def get(self, request):

        # Creamos una instancia del formulario personalizado.
        form = DatosForm()

        # Preparamos los datos del formulario para pasar al contexto.
        context = {
            'form': form 
        }

        # Mostramos en la página el formulario de registro de informacion.
        return render(request, 'home.html', context) 
    
    # Método POST para procesar los datos del formulario cuando se envía.
    def post(self, request):
        pass