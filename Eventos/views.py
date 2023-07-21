from django.shortcuts import render
from .models import Evento

def eventos(request):
    """Guardamos los eventos de los modelos en una variable"""
    eventos=Evento.objects.all()
    """Renderizamos pasando como parameros los eventos"""
    return render(request, "eventos/eventos.html", {"eventos":eventos})
