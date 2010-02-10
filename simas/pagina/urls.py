from django.conf.urls.defaults import *
import os
from django.conf import settings
from pagina.models import Noticia


urlpatterns = patterns('simas.pagina.views',
    (r'^noticia/$', 'ver_noticia'),

)
