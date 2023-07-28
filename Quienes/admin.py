from django.contrib import admin
from .models import Colma2

class Colma2Admin(admin.ModelAdmin):
    
    readonly_fields=("created","updated")
    
    
admin.site.register(Colma2, Colma2Admin)
