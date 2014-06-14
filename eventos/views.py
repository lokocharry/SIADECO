# Create your views here.
# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from eventos.models import *
from django.db.models import Count
from geraldo.generators import PDFGenerator
from graphos.renderers import highcharts
from graphos.sources.simple import SimpleDataSource

def mis_logros(request):
  lst=Resultado.objects.filter(deportista__usuario=request.user.id)
  data =  [
        ['Logros', 'Total', 'Realizado', 'No Realizado', 'En espera'],
        ['Logros',
        Resultado.objects.filter(deportista__usuario=request.user.id).count(),
        Resultado.objects.filter(deportista__usuario=request.user.id, resultado='L').count(),
        Resultado.objects.filter(deportista__usuario=request.user.id, resultado='N').count(),
        Resultado.objects.filter(deportista__usuario=request.user.id, resultado='E').count()]
    ]
  cht = highcharts.ColumnChart(SimpleDataSource(data=data))
  return render_to_response('misLogros.html',{'list':lst, 'chart': cht}, context_instance=RequestContext(request))

def evento_report(request):
  resp = HttpResponse(mimetype='application/pdf')
  data = Evento.objects.all()
  report = ReportEvento(queryset=data)
  report.generate_by(PDFGenerator, filename=resp)
  return resp

def logro_report(request):
  resp = HttpResponse(mimetype='application/pdf')
  data = Logro.objects.all()
  report = ReportLogro(queryset=data)
  report.generate_by(PDFGenerator, filename=resp)
  return resp

def lugeven_report(request):
  resp = HttpResponse(mimetype='application/pdf')
  data = LugEven.objects.all()
  report = ReportLugEven(queryset=data)
  report.generate_by(PDFGenerator, filename=resp)
  return resp

def resultado_report(request):
  resp = HttpResponse(mimetype='application/pdf')
  data = Resultado.objects.all()
  report = ReportResultado(queryset=data)
  report.generate_by(PDFGenerator, filename=resp)
  return resp