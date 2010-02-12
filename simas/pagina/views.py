 # -*- coding: UTF-8 -*-
from pagina.models import *
from datetime import date
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from urllib2 import urlopen

hoy = date.today()
URL = "http://www.elpueblopresidente.com/servicios/wsmoneda.php?dia=%s&mes=%s&ano=%s&formato=jsonvalido" % (hoy.day, hoy.month, hoy.year)

def handles_uploaded_file(f):
	file_name = os.path.join(settings.ATTACHMENT_PATH, f.titulo)
	destination = open(file_name, 'wb+')
	for chunk in f.chunk():
		destination.write(chunk)
	destination.close()


def index(request):
    noticias = Noticia.objects.all()[:3]
    actividades = Actividad.objects.all()[:3]
    #Tipo de cambio. Powered By El Pueblo Presidente \m/
    #TODO: Fix this shit. Esperar que EPP de bien las fechas. :-)
    json = urlopen(URL).read()
    tipos_de_cambios= simplejson.loads(json)['tipodecambioni']
    seccion=Seccion.objects.all()
    subseccion=Subseccion.objects.all()
    dict = {'noticias': noticias, 'actividades': actividades,
            'seccion':seccion,'subseccion':subseccion,
            'tipos_de_cambios': tipos_de_cambios}
    return render_to_response('pagina/index.html', dict,context_instance=RequestContext(request))
    	
def ver_noticia(request, id_noticia):
    noticia = Noticia.objects.get(id=id_noticia)
    dict = {'noticias': noticia}
    return render_to_response('pagina/noticia.html', dict,
                              context_instance=RequestContext(request))

def ver_actividad(request, id_actividad):
    actividad = Actividad.objects.get(id=id_actividad)
    dict = {'actividad': actividad}
    return render_to_response('pagina/actividad.html', dict,
                              context_instance=RequestContext(request)) 
