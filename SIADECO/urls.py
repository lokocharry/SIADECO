from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SIADECO.views.home', name='home'),
    # url(r'^SIADECO/', include('SIADECO.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(  r'^', include( 'noticias.urls' ) ),
    url(  r'^', include( 'deportes.urls' ) ),
    url(  r'^', include( 'eventos.urls' ) ),
    url(  r'^', include( 'usuarios.urls' ) ),
    url(r'^deportista/create', 'usuarios.views.nuevo_deportista'),
    url(r'^entrenador/create', 'usuarios.views.nuevo_entrenador'),
    url(r'^administrador/create', 'usuarios.views.nuevo_administrador'),
    url(r'^login', 'usuarios.views.log_in'),
    url(r'^logout', 'usuarios.views.log_out'),
    url(r'^verNoticias', 'noticias.views.ver_noticias'),
    url(r'^misLogros', 'eventos.views.mis_logros'),
    url(r'^deporte-report/$', 'deportes.views.deporte_report'),
    url(r'^modalidad-report/$', 'deportes.views.modalidad_report'),
    url(r'^depmod-report/$', 'deportes.views.depmod_report'),
    url(r'^evento-report/$', 'eventos.views.evento_report'),
    url(r'^logro-report/$', 'eventos.views.logro_report'),
    url(r'^lugeven-report/$', 'eventos.views.lugeven_report'),
    url(r'^resultado-report/$', 'eventos.views.resultado_report'),
    url(r'^acercaDe/$', 'usuarios.views.about'),
    url(r'home', 'usuarios.views.index'),
)
