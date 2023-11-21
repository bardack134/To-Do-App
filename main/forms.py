from django import forms

 # Importamos el modelo 'Datos' desde el archivo 'models.py' en la misma carpeta
from .models import Datos

#definicion de la clase del formulario
class DatosForm(forms.ModelForm):
    class Meta:
        # Asociamos el formulario con el modelo 'Datos'
        model=Datos

        # Incluimos todos los campos del modelo en el formulario
        fields="__all__"