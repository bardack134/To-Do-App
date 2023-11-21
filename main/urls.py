

from django.urls import path

from . import views



app_name='Main'
# Define las URL de tu aplicación

urlpatterns = [
    path('', views.home, name='todo'),
    
]

