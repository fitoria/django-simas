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
from django.db.models import Q
import re

hoy = date.today()
URL = "http://www.elpueblopresidente.com/servicios/wsmoneda.php?ano=%s&mes=%s&dia=%s&formato=jsonvalido&limite=5" % (hoy.year, hoy.month, hoy.day)

def index(request):
    '''Vista inicial'''
    noticias = Noticia.objects.order_by('-fecha')[:3]
    actividades = Actividad.objects.order_by('-fecha')[:4]
    categorias = Categoria.objects.all()
    enlaces = Link.objects.all()
    dicc = {'noticias': noticias, 'actividades': actividades,
            'categorias': categorias, 'enlaces': enlaces}
            
    return render_to_response('pagina/index.html', dicc, 
                              context_instance=RequestContext(request))

def moneda_ajax(request):
    '''vista que retorna json de los prox 5 dias
    de moneda. Info gracias a elpueblopresidente.com'''
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
    
    return HttpResponse(simplejson.dumps(tipos_de_cambios), 
                        mimetype="application/javascript")
    	
def ver_noticia(request, id_noticia):
    '''vista de una noticia. Parametro url ID'''
    noticia = Noticia.objects.get(id=id_noticia)
    dicc = {'noticias': noticia}
    return render_to_response('pagina/noticia.html', dicc,
                              context_instance=RequestContext(request))

def ver_actividad(request, id_actividad):
    '''vista de una actividad. Parametro url ID'''
    actividad = Actividad.objects.get(id=id_actividad)
    dicc = {'actividad': actividad}
    return render_to_response('pagina/actividad.html', dicc, 
                              context_instance=RequestContext(request)) 

def actividades(request, ano=None, mes=None, dia=None, participante=None):
    '''vista de lista de Actividades'''
    if participante:
        if ano and mes and dia:
            try:
                fecha = date(int(ano), int(mes), int(dia))
            except:
                raise Http404
            
            lista_actividades = Actividad.objects.filter(fecha = fecha, 
                                                         participantes__user__username = participante)
            mensaje = "Actividades del dia de %s-%s-%s" % (fecha.day, 
                                                           fecha.month, fecha.year)
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

    anos = range(rango_anos['ano_minimo'].year, 
                 rango_anos['ano_maximo'].year + 1)
    participantes = UserProfile.objects.all()
    
    dicc = {'actividades': actividades, 'mensaje': mensaje,
            'dias': range(1,32), 'anos': anos, 
            'participantes': participantes}
    return render_to_response('pagina/actividades.html', dicc,
                              context_instance=RequestContext(request))
                              
def noticias(request, ano=None, mes=None, autor=None):
    '''Vista de lista de noticias'''
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

    dicc = {'noticias': noticias, 'mensaje': mensaje,
            'dias': range(1,32), 'anos': anos, 
            'autores': autores}
    return render_to_response('pagina/noticias.html', dicc,
                                context_instance=RequestContext(request))

def documentos(request, subseccion):
    '''Vista de lista de documentos, paginados.
    Parametros url: subseccion'''
    subseccion = get_object_or_404(Subseccion, slug=subseccion) 
    lista_documentos = Archivo.objects.filter(subseccion = subseccion).order_by('-id')

    paginator = Paginator(lista_documentos, 12)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        documentos = paginator.page(page)
    except (EmptyPage, InvalidPage):
        documentos = paginator.page(paginator.num_pages)

    dicc = {"documentos": documentos, "subseccion": subseccion}
    return render_to_response('pagina/documentos.html', dicc,
                                context_instance=RequestContext(request))
                                
def buscar(request):
    '''vista de busqueda de contactos'''
    query = request.GET.get('q', '')
    query = query.replace(",","")
    if query:
        separacion = re.split('\W+', query)
        qsets = []
        for palabra in separacion:
            qsets.append((Q(nombres__icontains=palabra) | Q(apellidos__icontains=palabra)))
        qsets = [reduce(lambda x,y: x&y, qsets, Q())]
        qdata = (
            #No muy seguro de hacer esto, pero bueno
    		#Q(tipo__nombre__icontains=query)|
    		Q(tel1__icontains=query)|
    		Q(tel2__icontains=query)|
    		Q(tel3__icontains=query)|
    		Q(cel1__icontains=query)|
    		Q(cel2__icontains=query)|
    		Q(email1__icontains=query)|
    		Q(email2__icontains=query)
    			)
        qsets.append(qdata)
        q = reduce(lambda x,y: x|y, qsets, Q()) 
        results = Contacto.objects.filter(q).distinct()
    else:
        results = []
    dicc = {"results": results, "query": query, "c": len(results)}
    return render_to_response("pagina/busquedas.html", dicc,
                               context_instance = RequestContext(request))

def contactos(request, organizacion = None, pais = None,
              tipo = None):
    '''Vista general de contactos.
    Parametros de url:
    contactos/organizacion/<id>
    contactos/pais/<slug>
    contactos/tipo/<id>'''

    if organizacion:
        lista_contactos = Contacto.objects.filter(organizacion__id = organizacion)
    elif pais:
        lista_contactos = Contacto.objects.filter(pais__slug = pais)
    elif tipo:
        lista_contactos = Contacto.objects.filter(tipo__id = tipo)
    else:
        lista_contactos = Contacto.objects.all()

    paginator = Paginator(lista_contactos, 10)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        contactos = paginator.page(page)
    except (EmptyPage, InvalidPage):
        contactos = paginator.page(paginator.num_pages)

    dicc = {"contactos": contactos}
    return render_to_response('pagina/contactos.html', dicc,
                                context_instance = RequestContext(request))

def ver_contacto(request, id):
    '''Vista para ver un contacto especifico'''
    contacto  = get_object_or_404(Contacto, id=id)
    return render_to_response('pagina/ver_contacto.html', 
                              {'contacto': contacto},
                              context_instance = RequestContext(request))
