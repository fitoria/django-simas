from django.conf.urls.defaults import *
import settings
from os import path as os_path
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^django_simas/', include('django_simas.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^perfiles/', include('profiles.urls')),
    (r'^cuenta/login/$', 'django.contrib.auth.views.login', {'template_name': 'profiles/login.html'}),
    (r'^cuenta/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    (r'^', include('pagina.urls')),
    (r'^$', 'pagina.views.index'),
)
if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^archivos/(.*)$', 'django.views.static.serve',
                             {'document_root': os_path.join(settings.MEDIA_ROOT)}),
                           )

