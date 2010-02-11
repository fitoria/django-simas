from pagina.models import *
from datetime import date
from django.shortcuts import render_to_response

# Create your views here.

def handles_uploaded_file(f):
	file_name = os.path.join(settings.ATTACHMENT_PATH, f.titulo)
	destination = open(file_name, 'wb+')
	for chunk in f.chunk():
		destination.write(chunk)
	destination.close()


def index(request):
    return render_to_response('pagina/index.html')
    	
def ver_noticia(request):
    noti=Noticia.objects.all()
    return render_to_response('pagina/noticias_izq.html',locals())

def ver_actividad(request):
    activ=Actividad.objects.all()
    render_to_response('pagina/actividad_der.html',locals()) 
    
      
def ver_documento(request):
    docu=Archivo.objects.filter(subcategoria__nombre__icontains='formatos')
#    nada = docu.
    return render_to_response('pagina/documentos.html',locals())
 
def test(request):
    return render_to_response('pagina/test.html')

def test_dos(request):
    return render_to_response('pagina/test_dos.html')
