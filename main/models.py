from django.db import models



# Define un modelo llamado 'Datos'
class Datos(models.Model):
    # Define un campo 'titulo' de tipo CharField en el modelo.
    titulo = models.CharField(max_length=100)

    # Define un campo 'descripcion' de tipo TextField en el modelo.
    # Este campo se utilizará para almacenar textos más largos, sin una longitud máxima predefinida.
    descripcion = models.TextField()

    
    # Este campo se utilizará para almacenar fechas y horas. 'auto_now_add=True' establece la fecha automáticamente al agregar un nuevo registro.
    fecha = models.DateTimeField(auto_now_add=True)

    # campo para verficiar si la tarea ha sido comletada o no.
    completado=models.BooleanField(default=False)
