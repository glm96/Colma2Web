from django.db import models
"""Configuramos los modelos para los eventos
Fijarse en el tipo de cada atributo
Las imagenes se cargan de la carpeta Media/eventos
created y updated se configuran automaticamente para saber cuando se creó el evento y cuando se modificó"""
class Evento(models.Model):
    
    nombre=models.CharField(max_length=50)
    contenido=models.CharField(max_length=150)
    imagen=models.ImageField(upload_to='eventos')
    fecha=models.CharField(max_length=15)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    """Le decimos que nombre en singular y plural tenga esta clase"""
    class Meta:
        verbose_name='evento'
        verbose_name_plural='eventos'
    """Le decimos que nos devuelva el nombre de cada evento"""    
    def __str__(self):
        return self.nombre