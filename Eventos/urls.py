from django.urls import path
from . import views
"""Estas dos importaciones son para poder llegar a las urls de las imagenes"""
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.eventos, name="Eventos"),
    
]

"Esta linea es para declarar donde queramos que coja las imagenes"
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

