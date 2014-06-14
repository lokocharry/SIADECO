from django.conf.urls import patterns, include, url
from bsct.urls import URLGenerator
from deportes.models import *

bsct_patterns1 = URLGenerator(Deporte).get_urlpatterns( paginate_by = 10 )
bsct_patterns2 = URLGenerator(Modalidad).get_urlpatterns( paginate_by = 10 )
bsct_patterns3 = URLGenerator(DepMod).get_urlpatterns( paginate_by = 10 )

urlpatterns = patterns( '',
        url( '', include( bsct_patterns1 ) ),
        url( '', include( bsct_patterns2 ) ),
        url( '', include( bsct_patterns3 ) )
)