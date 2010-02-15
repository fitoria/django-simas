from pagina.models import *
from datetime import date
def sidebar(request):
    #documentos, cumpleanos, dias feriados
    secciones = Seccion.objects.all()
    subsecciones = Subseccion.objects.all()
    dias = DiasFeriados.objects.filter(fecha__gte = date.today())
    cumpleanos = UserProfile.objects.filter(fecha__gte = date.today())
    dict = {'secciones': secciones, 'subsecciones': subsecciones,
            'dias': dias, 'cumpleanos': cumpleanos}
    return dict
