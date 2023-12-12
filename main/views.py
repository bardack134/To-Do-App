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
        # obtengo los datos que estan en la base de datos
        datos = Datos.objects.all()

        # Creamos una instancia del formulario personalizado.
        form = DatosForm()

        # Preparamos los datos del formulario para pasar al contexto y los datos obtenidos 
        # 
        # de la base de datos
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
    

#Funcion para borrar un registro
def Delete(request, item_id):
    # dato_item=Datos.objects.get(id=request.POST['id'])
    dato_item=Datos.objects.get(id=item_id)
    
    # usamos funcion delete para borrar un objeto de la base de datos
    dato_item.delete()

    # Mostramos un mensaje de éxito.
    messages.info(request, 'Deleted successfully.')

    #redirigimos a la misma vista de registro
    return redirect(reverse('Main:registrar'))


# Definimos la función Update que toma como argumentos la solicitud HTTP y el ID del objeto a actualizar
def Update(request, item_id):
    # Usamos un bloque try-except para manejar posibles errores
    try:
        # Obtenemos el objeto que deseamos actualizar utilizando el método get() 
        # y pasando el ID del objeto como argumento
        dato_item=Datos.objects.get(id=item_id)
        
        # Actualizamos el campo 'titulo' del objeto con el nuevo título que se envió en la solicitud POST
        dato_item.titulo = request.POST['nuevo_titulo']

        # Actualizamos el campo 'descripcion' del objeto con la nueva descripción que se envió en la solicitud POST
        dato_item.descripcion = request.POST['nuevo_descripcion']

        # Guardamos los cambios en la base de datos utilizando el método save() del objeto
        dato_item.save()
        
        # Mostramos un mensaje de éxito utilizando el método info() de messages
        messages.info(request, 'updated successfully.')

        # Redirigimos al usuario a la vista 'Main:registrar' utilizando la función redirect() y la función reverse()
        return redirect(reverse('Main:registrar'))

    # Si el objeto con el ID especificado no existe, el método get() lanzará una excepción Datos.DoesNotExist
    except Datos.DoesNotExist:
        # Mostramos un mensaje de error utilizando el método error() de messages
        messages.error(request, 'registered not found')


# vista para completar una tarea
def Complete(request, item_id):
        
        # Obtenemos el objeto que deseamos completar utilizando el método get() 
        # y pasando el ID del objeto como argumento
        dato_item=Datos.objects.get(id=item_id)

        # actulizamos el campo completado del elemento, cambiando su valor de false(default) a true
        dato_item.completado=True

        # Guardamos los cambios en la base de datos utilizando el método save() del objeto
        dato_item.save()

        # Mostramos un mensaje de éxito 
        messages.success(request, 'completed successfully.')

        # Redirigimos al usuario a la vista 'Main:registrar' utilizando la función redirect() y la función reverse()
        return redirect(reverse('Main:registrar'))

