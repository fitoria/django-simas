from django.contrib import admin
from pagina.models import *

class CategoriaAdmin(admin.ModelAdmin):
	pass

class LinkAdmin(admin.ModelAdmin):
	pass

class ArchivoAdmin(admin.ModelAdmin):
    class Media:
        js = ('../archivos/js/tiny_mce/tiny_mce.js',
              '../archivos/js/editores/textareas.js')

class NoticiaAdmin(admin.ModelAdmin):
    class Media:
        js = ('../archivos/js/tiny_mce/tiny_mce.js',
              '../archivos/js/editores/textareas.js')
    
class ActividadAdmin(admin.ModelAdmin):
    class Media:
        js = ('../archivos/js/tiny_mce/tiny_mce.js',
              '../archivos/js/editores/textareas.js')
    
class AreaAdmin(admin.ModelAdmin):
    pass

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'skype', 'cargo', 'area', 'celular']
    list_filter = ['area']
    ordering = ['user', 'area']

class DiasFeriadosAdmin(admin.ModelAdmin):
    pass

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(DiasFeriados, DiasFeriadosAdmin)
admin.site.register(Archivo, ArchivoAdmin)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Actividad, ActividadAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
