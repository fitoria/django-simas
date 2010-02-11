from pagina.models import *
from datetime import date
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.

def handles_uploaded_file(f):
	file_name = os.path.join(settings.ATTACHMENT_PATH, f.titulo)
	destination = open(file_name, 'wb+')
	for chunk in f.chunk():
		destination.write(chunk)
	destination.close()


def index(request):
    noticias = Noticia.objects.all()[:3]
    actividades = Actividad.objects.all()[:3]
    dict = {'noticias': noticias, 'actividades': actividades}
    return render_to_response('pagina/index.html', dict,context_instance=RequestContext(request))
    	
def noticias(request):
    noticias = Noticia.objects.all()
    dict = {'noticias': noticias}
    return render_to_response('pagina/noticias.html', dict)

def actividades(request):
    actividades = Actividad.objects.all()
    dict = {'actividades': actividades}
    render_to_response('pagina/actividades.html', dict) 
      
def ver_documento(request):
    docu=Archivo.objects.filter(subcategoria__nombre__icontains='formatos')
    return render_to_response('pagina/documentos.html',locals())
