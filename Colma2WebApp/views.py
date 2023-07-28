from django.shortcuts import render, HttpResponse


def home(request):
    
    return render(request, "Colma2WebApp/home.html")







