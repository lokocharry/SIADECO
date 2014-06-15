from django.db import models
from django.core.urlresolvers import reverse
from bsct.models import BSCTModelMixin

# Create your models here.

class Deporte(BSCTModelMixin, models.Model):
	nombre=models.CharField(max_length=20)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = "Deporte"
		verbose_name_plural = "Deportes"

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

class DepMod(BSCTModelMixin, models.Model):
	deportista=models.ForeignKey('usuarios.Persona', limit_choices_to={'tipo_persona': 'D'})
	modalidad=models.ForeignKey(Modalidad)

	def deportista_detail(self):
		return '%s' % ( self.deportista )

	def modalidad_detail(self):
		return '%s' % ( self.modalidad )

	def __unicode__(self):
		return u'%s %s' % (self.deportista, self.modalidad)

	class Meta:
		verbose_name = "Modalidad deportista"
		verbose_name_plural = "Modalidades deportistas"