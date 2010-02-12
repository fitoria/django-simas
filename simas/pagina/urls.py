from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns('pagina.views',
    (r'^index/$', 'index'),
    (r'^noticia/(?P<noti>[^/]+)/$', 'noticias'),
    (r'^actividad/(?P<acti>[^/]+)/$', 'actividades'),
    (r'^documentos/$', 'ver_documento'),

)
