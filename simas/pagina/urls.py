from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns('pagina.views',
    (r'^index/$', 'index'),
    (r'^ajax/moneda/$', 'moneda_ajax'),
    (r'^noticia/(?P<id_noticia>\d+)/$', 'ver_noticia'),
    (r'^actividad/(?P<id_actividad>\d+)/$', 'ver_actividad'),
    (r'^actividades/(?P<ano>\d{4})/(?P<mes>\d{2})/(?P<dia>\d{1,2})/$', 'actividades'),
    (r'^actividades/(?P<ano>\d{4})/(?P<mes>\d{2})/$', 'actividades'),
    (r'^actividades/(?P<ano>\d{4})/$', 'actividades'),
    (r'^actividades/(?P<ano>\d{4})/(?P<mes>\d{2})/(?P<dia>\d{1,2})/participante/(?P<participante>\w+)/$', 'actividades'),
    (r'^actividades/(?P<ano>\d{4})/(?P<mes>\d{2})/participante/(?P<participante>\w+)/$', 'actividades'),
    (r'^actividades/(?P<ano>\d{4})/participante/(?P<participante>\w+)/$', 'actividades'),
    (r'^actividades/participante/(?P<participante>\w+)/$', 'actividades'),
    (r'^actividades/$', 'actividades'),
    # Noticias
    (r'^noticias/(?P<ano>\d{4})/(?P<mes>\d{2})/$', 'noticias'),
    (r'^noticias/(?P<ano>\d{4})/$', 'noticias'),
    (r'^noticias/(?P<ano>\d{4})/(?P<mes>\d{2})/autor/(?P<autor>\w+)/$', 'noticias'),
    (r'^noticias/(?P<ano>\d{4})/autor/(?P<autor>\w+)/$', 'noticias'),
    (r'^noticias/autor/(?P<autor>\w+)/$', 'noticias'),
    (r'^noticias/$', 'noticias'),
    #Documentos
    (r'^documentos/(?P<subseccion>[\w-]+)/$', 'documentos'),
    #Buscar contacto. REVISAR!
    #URL deberia de ser: /contactos/buscar/
    (r'^busqueda/$', 'buscar'),
    (r'^contactos/organizacion/(?P<organizacion>\d+)/$', 'contactos'),
    (r'^contactos/pais/(?P<pais>[\w-]+)/$', 'contactos'),
    (r'^contactos/tipo/(?P<tipo>\d+)/$', 'contactos'),
    (r'^contactos/ver/(?P<id>\d+)/$', 'ver_contacto'),
)
