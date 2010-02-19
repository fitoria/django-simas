 # -*- coding: UTF-8 -*-
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import Http404, HttpResponse
from django.db.models import Min, Max
from pagina.models import *
from datetime import date
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils import simplejson
from urllib2 import urlopen
from django.conf import settings

hoy = date.today()
URL = "http://www.elpueblopresidente.com/servicios/wsmoneda.php?ano=%s&mes=%s&formato=jsonvalido&limite=5" % (hoy.year, hoy.month)

def index(request):
    noticias = Noticia.objects.order_by('-fecha')[:3]
    actividades = Actividad.objects.order_by('-fecha')[:3]
    dict = {'noticias': noticias, 'actividades': actividades}
            
    return render_to_response('pagina/index.html', dict,context_instance=RequestContext(request))

def moneda_ajax(request):
    #Tipo de cambio. Powered By El Pueblo Presidente \m/
    json = urlopen(URL).read()
    tipos_de_cambios = simplejson.loads(json)['tipodecambioni']
    #####OLD WAY####
    #lista_cambios = simplejson.loads(json)['tipodecambioni']
    #hacemos el calculo de los dias
    #dia_tope = hoy.day + 4 
    #if len(lista_cambios) > (hoy.day+5):
    #    tipos_de_cambios = lista_cambios[hoy.day - 1:dia_tope]
    #else:
    #    tipos_de_cambios = lista_cambios[hoy.day - 1:]
    
    return HttpResponse(simplejson.dumps(tipos_de_cambios), mimetype="application/javascript")
    	
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
        if ano and mes:
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
            lista_noticias = Noticia.objects.filter(fecha__year = ano, fecha__month=mes)
            mensaje = "Noticias del mes de %s, %s" % (mes, ano)
        elif ano:
            lista_noticias = Noticia.objects.filter(fecha__year = ano)
            mensaje = "Noticia %s" % ano
        else:
            lista_noticias = Noticia.objects.all()
            mensaje = "Noticias"

    paginator = Paginator(lista_noticias, 10)

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

def documentos(request, subseccion):
    subseccion = get_object_or_404(Subseccion, slug=subseccion) 
    lista_documentos = Archivo.objects.filter(subseccion = subseccion)

    paginator = Paginator(lista_documentos, 25)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        documentos = paginator.page(page)
    except (EmptyPage, InvalidPage):
        documentos = paginator.page(paginator.num_pages)

    dict = {"documentos": documentos, "subseccion": subseccion}
    return render_to_response('pagina/documentos.html', dict,
                                context_instance=RequestContext(request))
