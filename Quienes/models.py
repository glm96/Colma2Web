from django.db import models

class Colma2(models.Model):
    
    nombre=models.CharField(max_length=50)
    origen=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=400)
    frase=models.CharField(max_length=100)
    foto=models.ImageField(upload_to='quienes')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Colma2"
        verbose_name_plural="Colma2"
        
    def __strs__(self):
        
        return self.nombre