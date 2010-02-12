from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns('pagina.views',
    (r'^index/$', 'index'),
    (r'^noticia/(?P<id_noticia>\d+)/$', 'ver_noticia'),
    (r'^actividad/(?P<id_actividad>\d+)/$', 'ver_actividad'),
)
