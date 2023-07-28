from django.urls import path
from . import views
"""Estas dos importaciones son para poder llegar a las urls de las imagenes"""
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.contacto, name="Contacto"),
    
   
]