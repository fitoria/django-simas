from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns('simas.pagina.views',
    (r'^index/$', 'index'),
    (r'^noticia/$', 'ver_noticia'),
    (r'^actividad/$', 'ver_actividad'),
    (r'^documentos/$', 'ver_documento'),
    (r'^test/$', 'test'),
    (r'^test/2/$', 'test_dos'),

)
