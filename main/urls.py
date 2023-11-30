

from django.urls import path

from main.views import Registrar

from . import views




app_name='Main'
# Define las URL de tu aplicación

urlpatterns = [
    path('', Registrar.as_view(), name='registrar'),

    # pasamos el id del objeto que queremos aeliminar como un str en nuestra url
    path('Delete/<str:item_id>', views.Delete, name='Delete'),

    path('Update/<str:item_id>', views.Update, name='Update'),
    
    path('Complete/<str:item_id>', views.Complete, name='Complete'),

]