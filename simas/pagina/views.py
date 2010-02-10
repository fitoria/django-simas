from pagina.models import *
from datetime import date
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage

# Create your views here.

def handles_uploaded_file(f):
	file_name = os.path.join(settings.ATTACHMENT_PATH, f.titulo)
	destination = open(file_name, 'wb+')
	for chunk in f.chunk():
		destination.write(chunk)
	destination.close()
	
def ver_noticia(request):
    noti=Noticia.objects.all()
    return render_to_response('pagina/noticias.html',locals())
    

