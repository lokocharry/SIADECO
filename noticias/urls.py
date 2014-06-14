from django.conf.urls import patterns, include, url
from bsct.urls import URLGenerator
from noticias.models import *

bsct_patterns = URLGenerator(Noticia).get_urlpatterns( paginate_by = 10 )

urlpatterns = patterns( '',
        url( '', include( bsct_patterns ) ) 
)