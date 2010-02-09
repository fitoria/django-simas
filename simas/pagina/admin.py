from django.contrib import admin
from pagina.models import *

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
#	list_filter = ['nombre',]

class LinkAdmin(admin.ModelAdmin):
    list_display = ['nombre','peso','categoria']
    list_filter = ['nombre']
    search_fields = ['nombre']
    
class ArchivoAdmin(admin.ModelAdmin):
    list_display = ['titulo','fecha','categoria','usuario']
    list_filter = ['titulo','usuario']
    search_fields = ['titulo']
    
    class Media:
        js = ['../archivos/js/tiny_mce/tiny_mce.js',
              '../archivos/js/editores/textareas.js']

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ['titulo','fecha','autor']
    list_filter = ['autor']
    search_fields = ['autor','titulo']
    
    class Media:
        js = ['../archivos/js/tiny_mce/tiny_mce.js',
              '../archivos/js/editores/textareas.js']
    
class ActividadAdmin(admin.ModelAdmin):
    list_display = ['titulo','fecha','lugar']
    list_filter = ['fecha','area']
    search_fields = ['area']
    class Media:
        js = ['../archivos/js/tiny_mce/tiny_mce.js',
              '../archivos/js/editores/textareas.js']
    
class AreaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']
    
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'skype', 'cargo', 'area', 'celular']
    list_filter = ['area']
    ordering = ['user', 'area']
    search_fields = ['user']

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
