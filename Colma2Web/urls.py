"""
URL configuration for Colma2Web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Colma2WebApp import views

from django.conf import settings
from django.views.static import serve
from django.urls import re_path

"""Aqui vamos a declarar las urls, que apuntan al proyecto en general y luego
que apuntan a cada una de las aplicaciones"""
"""La de '' apunta a las urls de la app Colma2WebApp"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Colma2WebApp.urls')),
    path('eventos/',include('Eventos.urls')),
    path('donativos/',include('Donativos.urls')),
    path('contacto/',include('Contacto.urls')),
    path('quienes/',include('Quienes.urls')),
    path('galeria/',include('Galeria.urls')),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]
