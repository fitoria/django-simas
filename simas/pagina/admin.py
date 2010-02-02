from django.contrib import admin
from pagina.models import *

class CategoriasAdmin(admin.ModelAdmin):
	pass

class LinksAdmin(admin.ModelAdmin):
	pass

class SubirAdmin(admin.ModelAdmin):
	pass

class NoticiasAdmin(admin.ModelAdmin):
    pass
    
class ActividadesAdmin(admin.ModelAdmin):
    pass
    
class AreaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Categorias, CategoriasAdmin)
admin.site.register(Links, LinksAdmin)
admin.site.register(Subir_archivos, SubirAdmin)
admin.site.register(Noticias, NoticiasAdmin)
admin.site.register(Actividades, ActividadesAdmin)
admin.site.register(Area, AreaAdmin)
