from pagina.models import *
from datetime import date
def sidebar(request):
    #documentos, cumpleanos, dias feriados
    secciones = Seccion.objects.all()
    subsecciones = Subseccion.objects.all()
    dias = DiasFeriados.objects.filter(fecha__gte = date.today())
    cumpleanos = UserProfile.objects.all()
    dict = {'secciones': secciones, 'subsecciones': subsecciones,
            'dias_sidebar': dias, 'cumpleanos': cumpleanos, 'mes': str(date.today().month)}
    return dict
