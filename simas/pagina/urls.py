from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns('pagina.views',
    (r'^index/$', 'index'),
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
                     
)
