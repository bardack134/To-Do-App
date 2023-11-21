

from django.urls import path

from main.views import Registrar

s



app_name='Main'
# Define las URL de tu aplicación

urlpatterns = [
    path('', Registrar.as_view(), name='registrar'),
    
]

