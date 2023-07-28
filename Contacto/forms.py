from django import forms
"""El text area en contenido es para que se represente ese campo como un cuadro de texto grande"""
class FormularioContacto(forms.Form):
    
    nombre=forms.CharField(label="Nombre", required=True)
    email=forms.CharField(label="Email", required=True)
    contenido=forms.CharField(label="Contenido", required=True, widget=forms.Textarea)