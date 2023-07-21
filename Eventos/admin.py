from django.contrib import admin
from .models import Evento
"""Configuramos que aparezca en el panel de administración la clase Evento (modelo)"""
class EventoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Evento,EventoAdmin)

