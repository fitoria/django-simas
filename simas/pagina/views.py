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
    	
def noticias(request, noti):
    noticias = Noticia.objects.get(id=noti)
    dict = {'noticias': noticias}
    return render_to_response('pagina/noticias.html', dict,context_instance=RequestContext(request))

def actividades(request, acti):
    actividad = Actividad.objects.get(id=acti)
    dict = {'actividad': actividad}
    return render_to_response('pagina/actividades.html', dict,context_instance=RequestContext(request)) 
      
def ver_documento(request):
    docu=Archivo.objects.filter(subseccion__nombre__icontains='Formato_contrato')
    return render_to_response('pagina/documentos.html',{'docu':docu},context_instance=RequestContext(request))
