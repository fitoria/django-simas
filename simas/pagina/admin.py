from django.contrib import admin
from pagina.models import *
from simas.pagina.autocomplete_admin import FkAutocompleteAdmin

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    list_filter = ['nombre']
    prepopulated_fields = {'slug': ('nombre', )}

class LinkAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'peso', 'categoria']
    list_filter = ['nombre']
    search_fields = ['nombre']
    
class ArchivoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha', 'usuario']
    list_filter = ['titulo', 'usuario']
    search_fields = ['titulo']
    
    class Media:
        js = ['../archivos/js/tiny_mce/tiny_mce.js',
              '../archivos/js/editores/textareas.js']

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha', 'autor']
    list_filter = ['autor']
    search_fields = ['autor', 'titulo']
    
    class Media:
        js = ['../archivos/js/tiny_mce/tiny_mce.js',
              '../archivos/js/editores/textareas.js']
    
class ActividadAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha', 'lugar']
    filter_horizontal = ('participantes',)
    list_filter = ['fecha', 'area']
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
    
class SeccionAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    prepopulated_fields = {'slug': ('nombre',)}

class SubseccionAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    prepopulated_fields = {'slug': ('nombre',)}

class TipoContactoAdmin(admin.ModelAdmin):
    pass
    
class ContactosAdmin(FkAutocompleteAdmin):
    related_search_fields = { 'organizacion': ('nombre',)}
    list_display = ['nombres', 'apellidos', 
                    'tel1', 'cel1', 'organizacion',
                    'dir1']
    search_fields = ['nombres', 'apellidos', 
                     'organizacion__nombre', 'tipo__nombre',
                     'tel1', 'tel2', 'tel3','cel1','cel2',
                     'email1','email2']
    list_display_links = ('nombres','apellidos', 'tel1')
#    class Media:
#        js = ['../archivos/js/tiny_mce/tiny_mce.js',
#              '../archivos/js/editores/textareas.js']            
class OrganizacionAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']
    class Media:
        js = ['../archivos/js/tiny_mce/tiny_mce.js',
              '../archivos/js/editores/textareas.js']

class PaisAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    prepopulated_fields = {'slug': ('nombre',)}

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(DiasFeriados, DiasFeriadosAdmin)
admin.site.register(Archivo, ArchivoAdmin)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Actividad, ActividadAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Seccion, SeccionAdmin)
admin.site.register(Subseccion, SubseccionAdmin)
admin.site.register(TipoContacto, TipoContactoAdmin)
admin.site.register(Contacto, ContactosAdmin)
admin.site.register(Organizacion, OrganizacionAdmin)
admin.site.register(Pais, PaisAdmin)
