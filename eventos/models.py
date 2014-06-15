from django.db import models
from usuarios.models import Persona
from deportes.models import Deporte
from django.core.urlresolvers import reverse
from bsct.models import BSCTModelMixin
from geraldo import Report, landscape, ReportBand, ObjectValue, SystemField, BAND_WIDTH, Label
from reportlab.lib.pagesizes import A5
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_RIGHT, TA_CENTER

# Create your models here.

class Evento(BSCTModelMixin, models.Model):
    nombre=models.CharField(max_length=40)
    TIPO_EVENTO=(
        ('R', 'Regional'),
        ('N', 'Nacional'),
        ('I', 'Internacional'),
    )
    tipo_evento=models.CharField(max_length=10, choices=TIPO_EVENTO)

    def tipo_evento_detail(self):
        if self.tipo_evento=='R':
            return 'Regional'
        if self.tipo_evento=='N':
            return 'Nacional'
        if self.tipo_evento=='I':
            return 'Internacional'

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

class Logro(BSCTModelMixin, models.Model):
    nombre=models.CharField(max_length=40)
    fecha=models.DateField()
    descripcion=models.TextField()

    def __unicode__(self):
        return self.nombre

	class Meta:
		verbose_name = "Logro"
		verbose_name_plural = "Logros"


class Lugar(BSCTModelMixin, models.Model):
	nombre=models.CharField(max_length=40)
	lugar=models.ForeignKey('self', blank=True, null=True, related_name='Lugar')

	def __unicode__(self):
		return self.nombre

	def lugar_detail( self ):
		return '%s' % ( self.lugar )

	class Meta:
		verbose_name = "Lugar"
		verbose_name_plural = "Lugares"

class LugEven(BSCTModelMixin, models.Model):
	fecha_inicio=models.DateField()
	fecha_fin=models.DateField()
	lugar=models.ForeignKey(Lugar)
	evento=models.ForeignKey(Evento)

	def lugar_detail( self ):
		return '%s' % ( self.lugar )

	def evento_detail( self ):
		return '%s' % ( self.evento )

	def __unicode__(self):
		return u'%s (%s)' % (self.evento, self.lugar)

	class Meta:
		verbose_name = "Lugar evento"
		verbose_name_plural = "Lugares evento"

class Resultado(BSCTModelMixin, models.Model):
    lugar_evento=models.ForeignKey(LugEven)
    logro=models.ForeignKey(Logro)
    deportista=models.ForeignKey(Persona, limit_choices_to={'tipo_persona': 'D'})
    deporte=models.ForeignKey(Deporte)
    RESULTADO=(
		('L', 'Logrado'),
		('N', 'No logrado'),
        ('E', 'En espera'),
	)
    resultado=models.CharField(max_length=20, choices=RESULTADO, null=True, blank=True)

    def __unicode__(self):
        return u'(%s) %s' % (self.deportista, self.logro)

    def lugar_detail( self ):
        return '%s' % ( self.lugar )

    def logro_detail( self ):
        return '%s' % ( self.logro )

    def lugar_evento_detail( self ):
        return '%s' % ( self.lugar_evento )

    def deportista_detail( self ):
        return '%s' % ( self.deportista )

    def deporte_detail( self ):
        return '%s' % ( self.deporte )

    def resultado_detail( self ):
        if self.resultado == 'L':
            return 'Logrado'
        if self.resultado=='N':
            return 'No logrado'
        if self.resultado=='E':
            return 'En espera'
        if self.resultado is None:
            return 'En espera'

	class Meta:
		verbose_name = "Resultado"
		verbose_name_plural = "Resultados"

