from django.db import models
from django.core.urlresolvers import reverse
from bsct.models import BSCTModelMixin
from geraldo import Report, landscape, ReportBand, ObjectValue, SystemField, BAND_WIDTH, Label
from reportlab.lib.pagesizes import A5
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_RIGHT, TA_CENTER

# Create your models here.

class Deporte(BSCTModelMixin, models.Model):
	nombre=models.CharField(max_length=20)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = "Deporte"
		verbose_name_plural = "Deportes"

class ReportDeporte(Report):
    title = 'Lista de Deportes'
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
            ObjectValue(attribute_name='nombre', left=3*cm),
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

class Modalidad(BSCTModelMixin, models.Model):
	nombre=models.CharField(max_length=20)
	deporte=models.ForeignKey(Deporte)

	def deporte_detail( self ):
		return '%s' % ( self.deporte )

	def __unicode__(self):
		return u'(%s) %s' % (self.deporte, self.nombre)

	class Meta:
		verbose_name = "Modalidad"
		verbose_name_plural = "Modalidades"

class ReportModalidad(Report):
    title = 'Lista de Modalidades'
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
            ObjectValue(attribute_name='nombre', left=3*cm),
            ObjectValue(attribute_name='deporte', left=5*cm),
            )

    class band_page_header(ReportBand):
    	height = 1.3*cm
    	elements = [
            SystemField(expression='%(report_title)s', top=0.1*cm, left=0, width=BAND_WIDTH,
                style={'fontName': 'Helvetica-Bold', 'fontSize': 14, 'alignment': TA_CENTER}),
            Label(text="ID", top=0.8*cm, left=0.5*cm),
            Label(text=u"Nombre", top=0.8*cm, left=3*cm),
            Label(text=u"Deporte", top=0.8*cm, left=3*cm),
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

class DepMod(BSCTModelMixin, models.Model):
	deportista=models.ForeignKey('usuarios.Persona', limit_choices_to={'tipo_persona': 'D'})
	modalidad=models.ForeignKey(Modalidad)

	def __unicode__(self):
		return u'%s %s' % (self.deportista, self.modalidad)

	class Meta:
		verbose_name = "Modalidad deportista"
		verbose_name_plural = "Modalidades deportistas"

class ReportDepMod(Report):
    title = 'Lista de Deportistas y sus Modalidades'
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
            ObjectValue(attribute_name='deportista', left=5*cm),
            ObjectValue(attribute_name='modalidad', left=5*cm),
            )

    class band_page_header(ReportBand):
    	height = 1.3*cm
    	elements = [
            SystemField(expression='%(report_title)s', top=0.1*cm, left=0, width=BAND_WIDTH,
                style={'fontName': 'Helvetica-Bold', 'fontSize': 14, 'alignment': TA_CENTER}),
            Label(text="ID", top=0.8*cm, left=0.5*cm),
            Label(text=u"Deportista", top=0.8*cm, left=3*cm),
            Label(text=u"Modalidad", top=0.8*cm, left=3*cm),
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