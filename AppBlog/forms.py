from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User



class AutorForm(forms.Form):
    nombre = forms.CharField (max_length = 80, label='Nombre Autor' )
    apellido = forms.CharField (max_length = 80, label='Apellido' )
    edad= forms.IntegerField (label='Edad')
    correo = forms.EmailField (max_length= 100, label='Correo')
    ubicacion = forms.CharField (max_length = 200, label='Ubicacion geografica')
    descripcion = forms.CharField (label='Descripcion', widget=forms.Textarea)

class ArticuloForm (forms.Form):
    titulo = forms.CharField (max_length = 200, label='Nombre Articulo')
    subtitulo = forms.CharField (max_length = 200, label='Subtitulo del Articulo')
    cuerpo = forms.CharField (label = 'Contenido del Articulo', widget=forms.Textarea)
    autorart = forms.CharField (max_length = 80, label='Nombre Autor')
    #fecha_publicacion = forms.DateField (label='Fecha de Publicacion')
    imagen = forms.ImageField(label="imagen", required=False)


class RegistroUsuarioForm(UserCreationForm):

    email= forms.EmailField(label="Email")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}#para cada uno de los campos del formulario, le asigna un valor vacio


#-------------------------  Editar Usiario ---------------------------  
class UserEditForm(UserCreationForm):

    first_name=forms.CharField(label='Modificar Nombre')
    last_name=forms.CharField(label='Modificar Apellido')
    email= forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput) 

    class Meta:
        model=User
        fields=["first_name", "last_name","email", "password1", "password2"]
        help_texts = {k:"" for k in fields}#para cada uno de los campos del formulario, le asigna un valor vacio


#------------------------- Crear Avatar ---------------------------  
class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")