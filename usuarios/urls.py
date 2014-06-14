from django.conf.urls import patterns, include, url
from bsct.urls import URLGenerator
from usuarios.models import *

bsct_patterns1 = URLGenerator(EPS).get_urlpatterns( paginate_by = 10 )
bsct_patterns2 = URLGenerator(FechaEntrenador).get_urlpatterns( paginate_by = 10 )
bsct_patterns3 = URLGenerator(Archivo).get_urlpatterns( paginate_by = 10 )
bsct_patterns4 = URLGenerator(Persona).get_urlpatterns( paginate_by = 10 )

urlpatterns = patterns( '',
        url( '', include( bsct_patterns1 ) ),
        url( '', include( bsct_patterns2 ) ),
        url( '', include( bsct_patterns3 ) ),
        url( '', include( bsct_patterns4 ) )
)