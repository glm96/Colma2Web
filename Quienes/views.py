from django.shortcuts import render
from .models import Colma2

def quienes(request):

    colma2=Colma2.objects.all()
    return render(request, "Quienes/quienes.html", {"colma2":colma2})
