from django.conf.urls import patterns, include, url
from bsct.urls import URLGenerator
from eventos.models import *

bsct_patterns1 = URLGenerator(Evento).get_urlpatterns( paginate_by = 10 )
bsct_patterns2 = URLGenerator(Logro).get_urlpatterns( paginate_by = 10 )
bsct_patterns3 = URLGenerator(Lugar).get_urlpatterns( paginate_by = 10 )
bsct_patterns4 = URLGenerator(LugEven).get_urlpatterns( paginate_by = 10 )
bsct_patterns5 = URLGenerator(Resultado).get_urlpatterns( paginate_by = 10 )

urlpatterns = patterns( '',
        url( '', include( bsct_patterns1 ) ),
        url( '', include( bsct_patterns2 ) ),
        url( '', include( bsct_patterns3 ) ),
        url( '', include( bsct_patterns4 ) ),
        url( '', include( bsct_patterns5 ) )
)