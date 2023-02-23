from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView



urlpatterns = [

    path ('', Inicio, name = 'inicio'),
    path ('autores/', autores, name = 'autores'),
    path ('crear_autor/', crearautor, name = 'crear_autor'),
    path ('articulos/', articulos, name='articulos'),
    path ('crear_articulo/', crear_articulo, name= 'crear_articulo'),    

##------------------- Busqueda titulo --------------------        
    path ('busquedatitulo/', busquedatitulo, name= 'busquedatitulo'),
    path ('buscar/', buscar, name= 'buscar'),

#------------------- leer / eliminar / editar --------------------    
    #path ('leerautor/<id>', leerautores, name='leerautores'),
    path ('eliminarautor/<id>', eliminarautor, name='eliminarautor'),
    path ('editarautor/<id>', editarautor , name='editarautor'),

    path ('leerarticulo/<id>', leerarticulo, name='leerarticulo'), 
    path ('eliminararticulo/<id>', eliminararticulo, name='eliminararticulo'),
    path ('editararticulo/<id>', editararticulo, name='editararticulo'),

#------------------- Borrar Autor / Articulo con vista --------------------    
    path ('autor/list/', autorList.as_view(), name='autor_list'),
    path ('autor/borrar/<pk>', autorDelete.as_view(), name= 'autor_borrar'),


    path ('articulo/list/', articuloList.as_view(), name='articulo_list'),
    path ('articulo/borrar/<pk>', articuloDelete.as_view(), name= 'articulo_borrar'),

#------------------- Registrar/ Ingresar / Salir Usuario --------------------    
    path ('registro/', registro, name= 'registro'),
    path ('ingresar/', ingresar_request, name='ingresar'),
    path ('logout/', LogoutView.as_view(), name='logout'),

#------------------- Editar perfil / Crear Avatar --------------------    
    path('editarperfil/', editarperfil, name='editarperfil'),
    path('agregarAvatar/', agregaravatar, name='agregarAvatar'),

#------------------------ Presentacion -------------------------    
    path('presentacion/', presentacion, name='presentacion' )
]