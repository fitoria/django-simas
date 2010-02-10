from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns('simas.pagina.views',
    (r'^noticia/$', 'ver_noticia'),
    (r'^test/$', 'test'),
    (r'^test/2/$', 'test_dos'),

)
