

from django.urls import path

from main.views import Registrar

from . import views




app_name='Main'
# Define las URL de tu aplicación

urlpatterns = [
    path('', Registrar.as_view(), name='registrar'),
    path('ObtenerDatos', views.ObtenerDatos, name='ObtenerDatos'),
    
]


