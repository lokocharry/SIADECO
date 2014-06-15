# Create your views here.
# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from eventos.models import *
from usuarios.models import Persona
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

  data2=[
      ['Eventos', 'Regional', 'Nacional', 'Internacional'],
      ['Eventos',
      Resultado.objects.filter(deportista__usuario=request.user.id, lugar_evento__evento__tipo_evento='R').count(),
      Resultado.objects.filter(deportista__usuario=request.user.id, lugar_evento__evento__tipo_evento='N').count(),
      Resultado.objects.filter(deportista__usuario=request.user.id, lugar_evento__evento__tipo_evento='I').count()
      ]
  ]
  data3=[
      ['Medallas', 'Oro', 'Plata', 'Bronce', 'Participación'],
      ['Medallas',
      Resultado.objects.filter(deportista__usuario=request.user.id, logro__nombre='Primer lugar', resultado='L').count(),
      Resultado.objects.filter(deportista__usuario=request.user.id, logro__nombre='Segundo lugar', resultado='L').count(),
      Resultado.objects.filter(deportista__usuario=request.user.id, logro__nombre='Tercer lugar', resultado='L').count(),
      Resultado.objects.filter(deportista__usuario=request.user.id, logro__nombre='Participación', resultado='L').count()
      ]
  ]
  cht2 = highcharts.ColumnChart(SimpleDataSource(data=data2))
  cht3 = highcharts.ColumnChart(SimpleDataSource(data=data3))
  return render_to_response('misLogros.html',{'list':lst, 'chart': cht, 'chart2': cht2, 'chart3': cht3}, context_instance=RequestContext(request))

def logros_deportista(request, ID):
  deportista=Persona.objects.get(id=ID)
  nombre=deportista.nombre+' '+deportista.apellido
  lst=Resultado.objects.filter(deportista=deportista)
  data =  [
        ['Logros', 'Total', 'Realizado', 'No Realizado', 'En espera'],
        ['Logros',
        Resultado.objects.filter(deportista=deportista).count(),
        Resultado.objects.filter(deportista=deportista, resultado='L').count(),
        Resultado.objects.filter(deportista=deportista, resultado='N').count(),
        Resultado.objects.filter(deportista=deportista, resultado='E').count()]
    ]
  cht = highcharts.ColumnChart(SimpleDataSource(data=data))
  data2=[
      ['Eventos', 'Regional', 'Nacional', 'Internacional'],
      ['Eventos',
      Resultado.objects.filter(deportista=deportista, lugar_evento__evento__tipo_evento='R').count(),
      Resultado.objects.filter(deportista=deportista, lugar_evento__evento__tipo_evento='N').count(),
      Resultado.objects.filter(deportista=deportista, lugar_evento__evento__tipo_evento='I').count()
      ]
  ]
  data3=[
      ['Medallas', 'Oro', 'Plata', 'Bronce', 'Participación'],
      ['Medallas',
      Resultado.objects.filter(deportista=deportista, logro__nombre='Primer lugar', resultado='L').count(),
      Resultado.objects.filter(deportista=deportista, logro__nombre='Segundo lugar', resultado='L').count(),
      Resultado.objects.filter(deportista=deportista, logro__nombre='Tercer lugar', resultado='L').count(),
      Resultado.objects.filter(deportista=deportista, logro__nombre='Participación', resultado='L').count()
      ]
  ]
  cht2 = highcharts.ColumnChart(SimpleDataSource(data=data2))
  cht3 = highcharts.ColumnChart(SimpleDataSource(data=data3))
  return render_to_response('misLogros.html',{'list':lst, 'chart': cht, 'chart2': cht2, 'nombre':nombre, 'chart3': cht3}, context_instance=RequestContext(request))

def lista_deportistas(request):
  lst=Persona.objects.filter(tipo_persona='D')
  print lst
  return render_to_response('logrosDeportista.html',{'list':lst}, context_instance=RequestContext(request))