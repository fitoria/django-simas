 # -*- coding: UTF-8 -*-
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import Http404
from django.db.models import Min, Max
from pagina.models import *
from datetime import date
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from urllib2 import urlopen

hoy = date.today()
URL = "http://www.elpueblopresidente.com/servicios/wsmoneda.php?mes=%s&ano=%s&formato=jsonvalido" % (hoy.month, hoy.year)

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
    json = urlopen(URL).read()
    lista_cambios = simplejson.loads(json)['tipodecambioni']
    #hacemos el calculo de los dias
    dia_tope = hoy.day + 4 
    if len(lista_cambios) > (hoy.day+5):
        tipos_de_cambios = lista_cambios[hoy.day - 1:dia_tope]
    else:
        tipos_de_cambios = lista_cambios[hoy.day - 1:]

    dict = {'noticias': noticias, 'actividades': actividades,
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

def actividades(request, ano=None, mes=None, dia=None, participante=None):
    if participante:
        if ano and mes and dia:
           try:
               fecha = date(int(ano), int(mes), int(dia))
           except:
               raise Http404
           lista_actividades = Actividad.objects.filter(fecha = fecha,
                                                       participantes__user__username = participante)
           mensaje = "Actividades del dia de %s-%s-%s" % (fecha.day, fecha.month, fecha.year)
        elif ano and mes:
           lista_actividades = Actividad.objects.filter(fecha__year = ano, fecha__month=mes,
                                                       participantes__user__username = participante)
           mensaje = "Actividades del mes de %s, %s" % (mes, ano)
        elif ano:
           lista_actividades = Actividad.objects.filter(fecha__year = ano, 
                                                        participantes__user__username = participante)
           mensaje = "Actividades de %s" % ano
        else:
            lista_actividades = Actividad.objects.filter(participantes__user__username = participante)
            mensaje = "Actividades de %s" % participante
    else:
        if ano and mes and dia:
           try:
               fecha = date(int(ano), int(mes), int(dia))
           except:
               raise Http404
           lista_actividades = Actividad.objects.filter(fecha = fecha)
           mensaje = "Actividades del dia de %s-%s-%s" % (fecha.day, fecha.month, fecha.year)
        elif ano and mes:
           lista_actividades = Actividad.objects.filter(fecha__year = ano, fecha__month=mes)
           mensaje = "Actividades del mes de %s, %s" % (mes, ano)
        elif ano:
           lista_actividades = Actividad.objects.filter(fecha__year = ano)
           mensaje = "Actividades %s" % ano
        else:
            lista_actividades = Actividad.objects.all()
            mensaje = "Actividades"
    
    paginator = Paginator(lista_actividades, 25)
    
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        actividades = paginator.page(page)
    except (EmptyPage, InvalidPage):
        actividades = paginator.page(paginator.num_pages)

    rango_anos = Actividad.objects.all().aggregate(ano_minimo = Min('fecha'),
                                                   ano_maximo = Max('fecha'))

    anos = range(rango_anos['ano_minimo'].year, rango_anos['ano_maximo'].year + 1)
    participantes = UserProfile.objects.all()
    
    dict = {'actividades': actividades, 'mensaje': mensaje,
            'dias': range(1,32), 'anos': anos, 
            'participantes': participantes}
    return render_to_response('pagina/actividades.html', dict,
                              context_instance=RequestContext(request))
                              
def noticias(request, ano=None, mes=None, autor=None):
    if autor:
        if ano and mes and dia:
           try:
               fecha = date(int(ano), int(mes),)
           except:
               raise Http404
           lista_noticias = Noticia.objects.filter(fecha = fecha,
                                                       autor__user__username = autor)
           mensaje = "Noticias del dia de %s-%s" % (fecha.month, fecha.year)
        elif ano and mes:
            lista_noticias = Noticia.objects.filter(fecha__year = ano, fecha__month=mes,
                                                           autor__user__username = autor)
            mensaje = "Noticias del mes de %s, %s" % (mes, ano)
        elif ano:
            lista_noticias = Noticia.objects.filter(fecha__year = ano, 
                                                    autor__user__username = autor)
            mensaje = "Noticias de %s" % ano
        else:
            lista_noticias = Noticia.objects.filter(autor__user__username = autor)
            mensaje = "Noticias de %s" % autor
    else:
        if ano and mes:
            try:
                fecha = date(int(ano), int(mes),)
            except:
                raise Http404
            lista_noticias = Noticia.objects.filter(fecha = fecha)
            mensaje = "Noticias del dia de %s-%s" % (fecha.month, fecha.year)
        elif ano and mes:
            lista_noticias = Noticia.objects.filter(fecha__year = ano, fecha__month=mes)
            mensaje = "Noticias del mes de %s, %s" % (mes, ano)
        elif ano:
            lista_noticias = Noticia.objects.filter(fecha__year = ano)
            mensaje = "Noticia %s" % ano
        else:
            lista_noticias = Noticia.objects.all()
            mensaje = "Noticias"

    paginator = Paginator(lista_noticias, 25)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        noticias = paginator.page(page)
    except (EmptyPage, InvalidPage):
        noticias = paginator.page(paginator.num_pages)

    rango_anos = Noticia.objects.all().aggregate(ano_minimo = Min('fecha'),
                                                    ano_maximo = Max('fecha'))

    anos = range(rango_anos['ano_minimo'].year, rango_anos['ano_maximo'].year + 1)
    autores = UserProfile.objects.all()

    dict = {'noticias': noticias, 'mensaje': mensaje,
            'dias': range(1,32), 'anos': anos, 
            'autores': autores}
    return render_to_response('pagina/noticias.html', dict,
                                context_instance=RequestContext(request))
