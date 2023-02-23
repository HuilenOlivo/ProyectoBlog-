from django import urls
from django.urls import path
from .views import *

urlpatterns = [
    path('enviar_mensaje/', enviar_mensaje, name='enviar_mensaje'),
    path('mensajes/', mensajes, name='mensajes'),
    path('mensajes_recibidos/', mensajes_recibidos, name='mensajes_recibidos'),
    path('eliminar_mensaje/<id>', eliminar_mensaje, name='eliminar_mensaje'),
    path('mostrar_mensaje/<id>', mostrar_mensaje, name='mostrar_mensaje'),
]