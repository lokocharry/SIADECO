# Create your views here.
# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from deportes.models import *
from geraldo.generators import PDFGenerator

def deporte_report(request):
  resp = HttpResponse(mimetype='application/pdf')
  data = Deporte.objects.all()
  report = ReportDeporte(queryset=data)
  report.generate_by(PDFGenerator, filename=resp)
  return resp

def modalidad_report(request):
  resp = HttpResponse(mimetype='application/pdf')
  data = Modalidad.objects.all()
  report = ReportModalidad(queryset=data)
  report.generate_by(PDFGenerator, filename=resp)
  return resp

def depmod_report(request):
  resp = HttpResponse(mimetype='application/pdf')
  data = DepMod.objects.all()
  report = ReportDepMod(queryset=data)
  report.generate_by(PDFGenerator, filename=resp)
  return resp