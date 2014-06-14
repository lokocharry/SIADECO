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

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

class ReportEvento(Report):
    title = 'Lista de Eventos'
    author = 'Alguien'

    page_size = landscape(A5)
    margin_left = 2*cm
    margin_top = 0.5*cm
    margin_right = 0.5*cm
    margin_bottom = 0.5*cm

    class band_detail(ReportBand):
        height = 0.5*cm
        elements=(
            ObjectValue(attribute_name='id', left=0.5*cm),
            ObjectValue(attribute_name='nombre', left=5*cm),
            )

    class band_page_header(ReportBand):
    	height = 1.3*cm
    	elements = [
            SystemField(expression='%(report_title)s', top=0.1*cm, left=0, width=BAND_WIDTH,
                style={'fontName': 'Helvetica-Bold', 'fontSize': 14, 'alignment': TA_CENTER}),
            Label(text="ID", top=0.8*cm, left=0.5*cm),
            Label(text=u"Nombre", top=0.8*cm, left=3*cm),
            SystemField(expression=u'Pagina %(page_number)d of %(page_count)d', top=0.1*cm,
                width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
            ]
    	borders = {'bottom': True}

	class band_page_footer(ReportBand):
		height = 0.5*cm
    	elements = [
            Label(text='Geraldo Reports', top=0.1*cm),
            SystemField(expression=u'Printed in %(now:%Y, %b %d)s at %(now:%H:%M)s', top=0.1*cm,
                width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
            ]
    	borders = {'top': True}

class Logro(BSCTModelMixin, models.Model):
    nombre=models.CharField(max_length=40)
    fecha=models.DateField()
    descripcion=models.TextField()

    def __unicode__(self):
        return self.nombre

	class Meta:
		verbose_name = "Logro"
		verbose_name_plural = "Logros"

class ReportLogro(Report):
    title = 'Lista de Logros'
    author = 'Alguien'

    page_size = landscape(A5)
    margin_left = 2*cm
    margin_top = 0.5*cm
    margin_right = 0.5*cm
    margin_bottom = 0.5*cm

    class band_detail(ReportBand):
        height = 0.5*cm
        elements=(
            ObjectValue(attribute_name='id', left=0.5*cm),
            ObjectValue(attribute_name='fecha', left=5*cm),
            ObjectValue(attribute_name='descripcion', left=5*cm),
            )

    class band_page_header(ReportBand):
    	height = 1.3*cm
    	elements = [
            SystemField(expression='%(report_title)s', top=0.1*cm, left=0, width=BAND_WIDTH,
                style={'fontName': 'Helvetica-Bold', 'fontSize': 14, 'alignment': TA_CENTER}),
            Label(text="ID", top=0.8*cm, left=0.5*cm),
            Label(text=u"Fecha", top=0.8*cm, left=3*cm),
            Label(text=u"Descripcion", top=0.8*cm, left=3*cm),
            SystemField(expression=u'Pagina %(page_number)d of %(page_count)d', top=0.1*cm,
                width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
            ]
    	borders = {'bottom': True}

	class band_page_footer(ReportBand):
		height = 0.5*cm
    	elements = [
            Label(text='Geraldo Reports', top=0.1*cm),
            SystemField(expression=u'Printed in %(now:%Y, %b %d)s at %(now:%H:%M)s', top=0.1*cm,
                width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
            ]
    	borders = {'top': True}

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

class ReportLugEven(Report):
    title = 'Lista de Eventos y sus Lugares'
    author = 'Alguien'

    page_size = landscape(A5)
    margin_left = 2*cm
    margin_top = 0.5*cm
    margin_right = 0.5*cm
    margin_bottom = 0.5*cm

    class band_detail(ReportBand):
        height = 0.5*cm
        elements=(
            ObjectValue(attribute_name='id', left=0.5*cm),
            ObjectValue(attribute_name='fecha_inicio', left=2*cm),
            ObjectValue(attribute_name='fecha_fin', left=2*cm),
            ObjectValue(attribute_name='lugar', left=2*cm),
            ObjectValue(attribute_name='evento', left=2*cm),
            )

    class band_page_header(ReportBand):
    	height = 1.3*cm
    	elements = [
            SystemField(expression='%(report_title)s', top=0.1*cm, left=0, width=BAND_WIDTH,
                style={'fontName': 'Helvetica-Bold', 'fontSize': 14, 'alignment': TA_CENTER}),
            Label(text="ID", top=0.8*cm, left=0.5*cm),
            Label(text=u"Fecha de inicio", top=0.8*cm, left=3*cm),
            Label(text=u"Fecha de final", top=0.8*cm, left=3*cm),
            Label(text=u"Lugar", top=0.8*cm, left=3*cm),
            Label(text=u"Evento", top=0.8*cm, left=3*cm),
            SystemField(expression=u'Pagina %(page_number)d of %(page_count)d', top=0.1*cm,
                width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
            ]
    	borders = {'bottom': True}

	class band_page_footer(ReportBand):
		height = 0.5*cm
    	elements = [
            Label(text='Geraldo Reports', top=0.1*cm),
            SystemField(expression=u'Printed in %(now:%Y, %b %d)s at %(now:%H:%M)s', top=0.1*cm,
                width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
            ]
    	borders = {'top': True}

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

	def lugar_detail( self ):
		return '%s' % ( self.lugar )

	def deportista_detail( self ):
		return '%s' % ( self.deportista )

	def deporte_detail( self ):
		return '%s' % ( self.deporte )

	def __unicode__(self):
		return u'(%s) %s' % (self.deportista, self.logro)

	class Meta:
		verbose_name = "Resultado"
		verbose_name_plural = "Resultados"

class ReportResultado(Report):
    title = 'Lista de Resultados'
    author = 'Alguien'

    page_size = landscape(A5)
    margin_left = 2*cm
    margin_top = 0.5*cm
    margin_right = 0.5*cm
    margin_bottom = 0.5*cm

    class band_detail(ReportBand):
        height = 0.5*cm
        elements=(
            ObjectValue(attribute_name='id', left=0.5*cm),
            ObjectValue(attribute_name='lugar_evento', left=2*cm),
            ObjectValue(attribute_name='logro', left=2*cm),
            ObjectValue(attribute_name='deportista', left=2*cm),
            ObjectValue(attribute_name='deporte', left=2*cm),
            ObjectValue(attribute_name='resultado', left=2*cm),
            )

    class band_page_header(ReportBand):
    	height = 1.3*cm
    	elements = [
            SystemField(expression='%(report_title)s', top=0.1*cm, left=0, width=BAND_WIDTH,
                style={'fontName': 'Helvetica-Bold', 'fontSize': 14, 'alignment': TA_CENTER}),
            Label(text="ID", top=0.8*cm, left=0.5*cm),
            Label(text=u"Lugar del evento", top=0.8*cm, left=3*cm),
            Label(text=u"Logro", top=0.8*cm, left=3*cm),
            Label(text=u"Deportista", top=0.8*cm, left=3*cm),
            Label(text=u"Deporte", top=0.8*cm, left=3*cm),
            Label(text=u"Resultado", top=0.8*cm, left=3*cm),
            SystemField(expression=u'Pagina %(page_number)d of %(page_count)d', top=0.1*cm,
                width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
            ]
    	borders = {'bottom': True}

	class band_page_footer(ReportBand):
		height = 0.5*cm
    	elements = [
            Label(text='Geraldo Reports', top=0.1*cm),
            SystemField(expression=u'Printed in %(now:%Y, %b %d)s at %(now:%H:%M)s', top=0.1*cm,
                width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
            ]
    	borders = {'top': True}

