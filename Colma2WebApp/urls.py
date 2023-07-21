from django.urls import path
from . import views
"""Estas dos importaciones son para poder llegar a las urls de las imagenes"""
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.home, name="Home"),
    path('quienes/', views.quienes, name="Quienes"),
    path('contacto/', views.contacto, name="Contacto"),
    path('donativos/', views.donativos, name="Donativos"),
]

"Esta linea es para declarar donde queramos que coja las imagenes"
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

