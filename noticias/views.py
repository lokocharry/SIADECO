# Create your views here.
# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from noticias.models import *
from chartit import DataPool, Chart

def ver_noticias(request):
  lst=Noticia.objects.all()[:4]
  return render_to_response('verNoticias.html',{'list':lst}, context_instance=RequestContext(request))

def ver_todas_noticias(request):
  lst=Noticia.objects.all()
  return render_to_response('verTodasNoticias.html',{'list':lst}, context_instance=RequestContext(request))

def detalle_noticia(request, ID):
	noticia=Noticia.objects.get(id=ID)
	return render_to_response('detallesNoticia.html',{'noticia':noticia}, context_instance=RequestContext(request))