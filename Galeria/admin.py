from django.contrib import admin
from .models import Galeria
"""Configuramos que aparezca en el panel de administración la clase Evento (modelo)"""
class GaleriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Galeria,GaleriaAdmin)
