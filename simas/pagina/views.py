from pagina.models import *
import datetime

# Create your views here.

def handles_uploaded_file(f):
	file_name = os.path.join(settings.ATTACHMENT_PATH, f.titulo)
	destination = open(file_name, 'wb+')
	for chunk in f.chunk():
		destination.write(chunk)
	destination.close()
	
def ver_archivos(request):
    archivos = Subir_archivos.objects.filter(fecha=date.now()) 
