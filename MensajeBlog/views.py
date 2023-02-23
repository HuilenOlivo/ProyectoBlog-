from django.shortcuts import render
from .forms import MensajeForm
from django.contrib.auth.models import User
from .models import Mensaje
from django.contrib.auth.decorators import login_required
from AppBlog.views import *

# Create your views here.
@login_required
def enviar_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            receptor = info ['receptor']
            mensaje = info ['mensaje']
            usuario = request.user
            fecha = info ['fecha']
            mensaje = Mensaje(usuario=usuario, receptor=receptor, mensaje=mensaje, fecha=fecha)
            mensaje.save()
            return render(request, 'AppBlog/mensajes.html', {'form': form, 'mensaje': 'Mensaje enviado', "avatar": obtenerAvatar(request)})
        else:
            return render(request, 'AppBlog/enviar_mensaje.html', {'form': form, 'mensaje': 'Mensaje no enviado', "avatar": obtenerAvatar(request)})
    else:
        form = MensajeForm()
        return render(request, 'AppBlog/enviar_mensaje.html', {'form': form, "avatar": obtenerAvatar(request)})

@login_required
def mensajes(request):
    return render(request, 'AppBlog/mensajes.html', { "avatar": obtenerAvatar(request)})

@login_required
def mensajes_recibidos(request):
    usuario = request.user
    mensajes = Mensaje.objects.filter(receptor=usuario)
    if len(mensajes) == 0:
        return render(request, 'AppBlog/mensajes_recibidos.html', {'mensaje': 'No tienes mensajes', "avatar": obtenerAvatar(request)})
    else:
        return render(request, 'AppBlog/mensajes_recibidos.html', {'mensajes': mensajes, "avatar": obtenerAvatar(request)})

@login_required
def eliminar_mensaje(request, id):
    mensaje = Mensaje.objects.get(id=id)
    mensaje.delete()
    mensajes = Mensaje.objects.filter(receptor=request.user)
    return render(request, 'AppBlog/mensajes_recibidos.html', {'mensajes': mensajes, 'mensaje': 'Mensaje eliminado', "avatar": obtenerAvatar(request)})

@login_required
def mostrar_mensaje(request, id):
    mensaje = Mensaje.objects.get(id=id)
    mensaje.leido=True
    mensaje.save()
    return render(request, 'AppBlog/mostrar_mensaje.html', {'mensaje': mensaje, "avatar": obtenerAvatar(request)})