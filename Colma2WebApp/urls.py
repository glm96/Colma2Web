from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="Home"),
    path('quienes/', views.quienes, name="Quienes"),
    path('eventos/', views.eventos, name="Eventos"),
    path('contacto/', views.contacto, name="Contacto"),
    path('donativos/', views.donativos, name="Donativos"),
]