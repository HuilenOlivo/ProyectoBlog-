from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        avatar=lista[0].imagen.url
    else:
        avatar="/media/avatars/descarga.jpeg"
    return avatar


def Inicio (request):
    return render (request,'AppBlog/inicio.html')

@login_required
def autores (request):
    return render (request, 'AppBlog/autores.html', { "avatar": obtenerAvatar(request)})




#------------------------------ Crear Articulo ------------------------------------ 
@login_required
def crear_articulo (request):
    if request.method == "POST":
        form=ArticuloForm (request.POST, request.FILES)

        if form.is_valid():
            informacionart=form.cleaned_data    
            titulo= informacionart['titulo']
            subtitulo= informacionart ['subtitulo']
            cuerpo= informacionart ['cuerpo']
            autorart= informacionart ['autorart']
            #fecha_publicacion = informacionart ['publicacion']
            imagen = request.FILES ['imagen']
            articulocreado= Articulo(titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, autor=autorart, imagen=imagen)
            articulocreado.save()
            articulos=Articulo.objects.all()
            return render(request, "AppBlog/articulos.html", {"articulos": articulos, "mensaje": "Articulo Creado Correctamente", "avatar": obtenerAvatar(request)})
        

        else:
            return render (request, 'AppBlog/crear_articulo.html', {"form": form, "mensaje": "Informacion no valida","avatar": obtenerAvatar(request)})

    else:
        formularioart=ArticuloForm()
        return render (request, 'AppBlog/crear_articulo.html', {'form': formularioart,"avatar": obtenerAvatar(request)})

#--------------------------------- Crear Autor ----------------------------------------------------
@login_required
def crearautor (request):
    if request.method=='POST':
        form= AutorForm (request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre= informacion['nombre']
            apellido= informacion ['apellido']
            edad= informacion ['edad']
            correo=informacion['correo']
            ubicacion=informacion['ubicacion']
            descripcion= informacion ['descripcion']
            autorcito= Autor (nombre=nombre, apellido=apellido, edad=edad, correo=correo, ubicacion=ubicacion, descripcion=descripcion)
            autorcito.save()
            autores= Autor.objects.all()
            return render (request, 'AppBlog/autores.html', {"autores": autores, "mensaje": "Autor Creado Correctamente","avatar": obtenerAvatar(request)})
        
        else:
            return render(request,'AppBlog/crear_autor.html', {"form": form, "mensaje": "Informacion no valida","avatar": obtenerAvatar(request)})

    else:
        formulario= AutorForm()
        return render (request, 'AppBlog/crear_autor.html', {'form': formulario,"avatar": obtenerAvatar(request)})

def usuario (request):
    return render (request,'AppBlog/crear_usuario.html')

#-----------------------------------Busqueda titulo------------------------------------------------------------------------------

@login_required
def busquedatitulo (request):
    return render (request, 'AppBlog/busquedatitulo.html', {'avatar':obtenerAvatar(request)} ) 

def buscar(request):
    
    titulo= request.GET["titulo"]
    if titulo!="":
        articulos= Articulo.objects.filter(titulo__icontains=titulo)
        return render(request, "AppBlog/resultadosbusqueda.html", {"articulos": articulos, 'avatar':obtenerAvatar(request)})
    else:
        return render(request, "AppBlog/busquedatitulo.html", {"mensaje": "Ingresar un Titulo para buscar",'avatar':obtenerAvatar(request)})

#---------------------------leer / eliminar / editar autor--------------------------------------------------------------

@login_required
def autores(request):
    autores=Autor.objects.all()
    return render (request, 'AppBlog/autores.html', {'autores': autores, "avatar": obtenerAvatar(request)})

@login_required
def eliminarautor (request, id):
    autor= Autor.objects.get(id=id)
    print (autor)
    autor.delete()
    autores= Autor.objects.all ()
    return render (request, 'AppBlog/autores.html', {'autores': autores, "mensaje": "Autor eliminado correctamente","avatar": obtenerAvatar(request)})

@login_required
def editarautor (request,id):
    autor = Autor.objects.get(id=id)
    if request.method=="POST":
        form= AutorForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            autor.nombre= informacion['nombre']
            autor.apellido= informacion ['apellido']
            autor.edad= informacion ['edad']
            autor.correo=informacion['correo']
            autor.ubicacion=informacion['ubicacion']
            autor.descripcion= informacion ['descripcion']
            autor.save()
            autor= Autor.objects.all()
            return render (request, 'AppBlog/autores.html', {"autores": autores, "mensaje": "Autor Editado Correctamente"})
        pass
        
    else:
        formulario= AutorForm(initial={"nombre":autor.nombre, "apellido":autor.apellido, "edad":autor.edad, "correo":autor.correo, "ubicacion":autor.ubicacion, "descripcion": autor.descripcion })
        return render (request, 'AppBlog/editarautor.html', {'form': formulario, 'autor': autor,  "avatar": obtenerAvatar(request)})

#-------------------------------leer / eliminar / editar  articulo---------------------------------------------------------------------------------

@login_required
def articulos(request):
    articulos=Articulo.objects.all()
    return render (request, 'AppBlog/Articulos.html', {'articulos': articulos, "avatar": obtenerAvatar(request)})

@login_required
def leerarticulo(request, id):
    post = Articulo.objects.get(id=id)
    if request.user.is_authenticated:
        return render(request, 'AppBlog/leerarticulo.html', {'post': post, "avatar": obtenerAvatar(request)})
    else:
        return render(request, 'Blogapp/mostrarPost.html', {'post': post})

@login_required
def eliminararticulo(request, id):
    articulo= Articulo.objects.get(id=id)
    print (articulo)
    articulo.delete()
    articulos= Articulo.objects.all ()
    return render (request, 'AppBlog/articulos.html', {'articulos': articulos, "mensaje": "Articulo eliminado correctamente","avatar": obtenerAvatar(request)})

@login_required
def editararticulo (request,id):
    articulo=Articulo.objects.get(id=id)
    if request.method=="POST":
        form= ArticuloForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            articulo.titulo= informacion['titulo']
            articulo.subtitulo= informacion ['subtitulo']
            articulo.cuerpo= informacion ['cuerpo']
            articulo.imagen= informacion ['imagen']
            articulo.save()
            articulos= Articulo.objects.all()
            return render (request, 'AppBlog/articulos.html', {"articulos": articulos, "mensaje": "Articulo Editado Correctamente", "avatar": obtenerAvatar(request)})
        pass
        
    else:
        formulario= ArticuloForm(initial={"titulo": articulo.titulo, "subtitulo":articulo.subtitulo, "cuerpo":articulo.cuerpo, "autor":articulo.autor, "imagen": articulo.imagen })
        return render (request, 'AppBlog/editararticulo.html', {'form': formulario, 'articulo': articulo, "avatar": obtenerAvatar(request)})


#------------------------- Boton borrar Autor --------------------------------------------------------------------------------------


class autorList(LoginRequiredMixin, ListView):
    model= Autor
    template_name= "AppCoder/autores.html"

class autorCreacion(LoginRequiredMixin,CreateView):
    model= Autor
    success_url= reverse_lazy("autor_list")
    fields=['nombre', 'apellido','edad', 'email']

class autorUpdate(LoginRequiredMixin,UpdateView):
    model= Autor
    success_url = reverse_lazy('autor_list')
    fields=['nombre', 'apellido','edad', 'email']

class autorDelete(LoginRequiredMixin,DeleteView):
    model= Autor
    success_url = reverse_lazy('autor_list')


#------------------------- Boton borrar articulo --------------------------------------------------------------------------------------


class articuloList(LoginRequiredMixin, ListView):
    model= Articulo
    template_name= "AppCoder/articulos.html"

class articuloCreacion(LoginRequiredMixin,CreateView):
    model= Articulo
    success_url= reverse_lazy("articulo_list")
    fields=['nombre', 'apellido','edad', 'email']

class articuloUpdate(LoginRequiredMixin,UpdateView):
    model= Articulo
    success_url = reverse_lazy('articulo_list')
    fields=['nombre', 'apellido','edad', 'email']

class articuloDelete(LoginRequiredMixin,DeleteView):
    model= Articulo
    success_url = reverse_lazy('articulo_list')



#------------------------- Registro Usuario---------------------------   
def registro (request):
    if request.method=="POST":
        form= RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render(request, "AppBlog/inicio.html", {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "AppBlog/registro.html", {"form": form, "mensaje":"Error al crear el usuario"})
    else:
        form= RegistroUsuarioForm()
        return render(request, "AppBlog/registro.html",{"form": form})


#------------------------- Ingresar Usuario---------------------------  
def ingresar_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave)#verifica si el usuario existe, si existe, lo devuelve, y si no devuelve None 
            if usuario is not None:
                login(request, usuario)
                return render(request, "AppBlog/inicio.html", {"mensaje":f"Usuario {usu} logueado correctamente"})
            else:
                return render(request, "AppBlog/ingresar.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, "AppBlog/ingresar.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request, "AppBlog/ingresar.html", {"form": form})


#------------------------- Editar Perfil --------------------------- 
@login_required 
def editarperfil(request):
    usuario=request.user

    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]            
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]

            usuario.save()
            return render(request, "AppBlog/inicio.html", {"mensaje":f"Usuario {usuario.username} editado correctamente", "avatar": obtenerAvatar(request)})
        else:
            return render(request, "AppBlog/editarperfil.html", {"form": form, "nombreusuario":usuario.username, "avatar": obtenerAvatar(request)})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "AppBlog/editarperfil.html", {"form": form, "nombreusuario":usuario.username, "avatar": obtenerAvatar(request)})


#------------------------- Crear Avatar ---------------------------  
def agregaravatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar.save()
            return render(request, "AppBlog/inicio.html", {"mensaje":f"Avatar agregado correctamente","avatar": obtenerAvatar(request)})
        else:
            return render(request, "AppBlog/agregarAvatar.html", {"form": form, "usuario": request.user, "mensaje":"Error al agregar el avatar"})
    else:
        form=AvatarForm()
        return render(request, "AppBlog/agregarAvatar.html", {"form": form, "usuario": request.user, "avatar": obtenerAvatar(request)})


#------------------------ Presentacion -------------------------  
def presentacion (request):
    return render (request,'AppBlog/presentacion.html', { "avatar": obtenerAvatar(request)})