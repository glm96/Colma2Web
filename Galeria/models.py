from django.db import models

class Galeria(models.Model):
    
    
    descripcion=models.CharField(max_length=400)
    imagen=models.ImageField(upload_to='galeria')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    
    class Meta:
        verbose_name='galeria'
        verbose_name_plural='galeria'
        
    def __str__(self):
        return self.descripcion
