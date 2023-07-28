from django.shortcuts import render
from .models import Galeria

def galeria(request):
    
    galeria=Galeria.objects.all()
    return render(request, "Galeria/galeria.html",{"galeria":galeria})
