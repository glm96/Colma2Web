from django.shortcuts import render, HttpResponse


def home(request):
    
    return render(request, "Colma2WebApp/home.html")

def quienes(request):

    return render(request, "Colma2WebApp/quienes.html")


def contacto(request):
    
    return render(request, "Colma2WebApp/contacto.html")

def donativos(request):
    
    return render(request, "Colma2WebApp/donativos.html")
