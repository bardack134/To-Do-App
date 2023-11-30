# Importamos los elementos necesarios de Django para manejar los formularios y la vista.
from django import forms

 # Importamos el modelo 'Datos' desde el archivo 'models.py' en la misma carpeta
from .models import Datos

#definicion de la clase del formulario
class DatosForm(forms.ModelForm):
    #cambiamos los nombres de la clase del formulario al ingles
    titulo = forms.CharField(label='Title',  max_length=100)

    descripcion = forms.CharField(label='Description', widget=forms.Textarea)

    class Meta:
        # Asociamos el formulario con el modelo 'Datos'
        model=Datos

        # excluimos el campo completado de nuestro formulario
        exclude = ['completado']
        
        # # Incluimos todos los campos del modelo en el formulario
        # fields="__all__"