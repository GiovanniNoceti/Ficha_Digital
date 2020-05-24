from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render 

class Persona(object):

    def __init__(self, name, lastname):

        self.name=name
        self.lastname=lastname

def saludo(request): #primera vista web 
    
    #declaro variable para darle valores al objeto
    P1=Persona("Elena","Noceti")

    #comentamos para el ejemplo del IF
    #temas_lista=["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
    
    #Para el condicional if se eliminan los datos de la lista
    temas_lista=[]

    #Variables simples para nombre y apellido
    #nombre="Giovanni"
    #apellido="Noceti"
    fecha_ahora= datetime.datetime.now()

    #Cargar una platilla en forma manual, pero no es la mejor forma
    #En un proyecto grande se usarán muchas platilla y no solo una, 
    # por lo tato no se pueden estar cerrando constantemente. 
    # Crearemos un loader (cargador de muchas plantilla) 
    #Doc_Externo = open("C:/Users/Administrador/Documents/ProyectosDjango/Proyecto1/Proyecto1/Plantillas/mi_plantilla.html")

    #le pasamos por parametros usando un Template
    #plt=Template(Doc_Externo.read())
    #Doc_Externo.close()
    
    Doc_Externo=loader.get_template('mi_plantilla.html')

    #Manejamos diccionario en el contexto y agregaremos una lista pero ahora con una variable con la lista
    #ctx=Context({"nombre_persona":P1.name, "apellido_persona":P1.lastname, "fecha":fecha_ahora, "temas":temas_lista})

    Tipo_Letra= Doc_Externo.render({"nombre_persona":P1.name, "apellido_persona":P1.lastname, "fecha":fecha_ahora, "temas":temas_lista})

    return HttpResponse(Tipo_Letra)

    #antes era el código y se simplificó más arriba"""
    #<html>
    #<body>
    #<h1>
    #Hola Gio, esta es mi primera página con Django
    #</h1>
    #</body>
    #</html>"""
    
    #Manejamos un diccionario en el contexto
    #ctx=Context({"nombre_persona":P1.name, "apellido_persona":P1.lastname, "fecha":fecha_ahora})

    #Manejamos diccionario en el contexto y agregaremos una lista
    #ctx=Context({"nombre_persona":P1.name, "apellido_persona":P1.lastname, "fecha":fecha_ahora, "temas":["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]})
    
    #Tipo_Letra= plt.render(ctx)
    
def despedida(request):

    return HttpResponse("Despedida de mi primera página con Django")

def fecha(request):

    Fecha_Actual = datetime.datetime.now()

    Muestra_Fecha = """
    <html>
    <body>
    <h2>
    Fecha y Hora %s
    </h2>
    </body>
    </html>""" % Fecha_Actual
    
    return HttpResponse(str(Muestra_Fecha))

#rescatamos 1 parametro desde la URl
def calculaEdad(request,agno):

        edadActual=1
        periodo=agno-2020
        edadFutura=edadActual+periodo

        muestraEdad="<html><body><h2>En el año %s tendrás %s años" %(agno, edadFutura)

        return HttpResponse(muestraEdad)

#rescatamos 2 parametro desde la URl
def calculaEdad2(request,edad,agno):

        #edadActual=1
        periodo=agno-2020
        edadFutura=edad+periodo

        muestraEdad2="<html><body><h2>En el año %s tendrás %s años" %(agno, edadFutura)

        return HttpResponse(muestraEdad2)
