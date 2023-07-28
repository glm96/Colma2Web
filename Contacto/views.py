from django.shortcuts import render,redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

"""Guardamos el formulario en una variable y lo pasamos como parámtero al renderizarlo"""
def contacto(request):

    formulario=FormularioContacto()
    """Si se ha pulsado el boton de enviar (POST)"""
    if request.method=="POST":
        formulario=FormularioContacto(data=request.POST)
        """Y el formulario es válido, guardamos en variables la informacion introducida en el formulario"""
        if formulario.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")
            """Configuramos el envio del email
            primer argumento es el asunto
            segundo argumento es el mensaje
            el tercer argumento es de quién viene que lo dejamos vacío porque ya sabemos que viene de la web
            el cuarto argumento es el email al que vamos a enviar el email
            Por último se declara si queremos que se pueda contestar al email recibido, dirigiendonos al mail que nos ha enviado ese mail"""
            
            email=EmailMessage("Mensaje de Colma2Web",
                               "El usuario con nombre {} con el email {} escribe lo siguiente: \n\n {}" .format(nombre,email,contenido),
                                "",["josemarync96@hotmail.es"], reply_to=[email])
                                
                       
            """Si se puede enviar el email"""  
            try:
                
                email.send()      
            
                """Mandamos a la url como parametro 'valido' para realizar una acción en el html """
                return redirect("/contacto/?valido")
                
                """Si no se puede enviar el mail"""
            except:
                """Mandamos a la url como parametro 'novalido' para realizar una acción en el html """
                
                return redirect("/contacto/?novalido")
        
    return render(request, "Contacto/contacto.html", {"formulario":formulario})
