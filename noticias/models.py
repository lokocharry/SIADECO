from django.db import models
from usuarios.models import Persona
from django.core.urlresolvers import reverse
from bsct.models import BSCTModelMixin

# Create your models here.

class Noticia(BSCTModelMixin, models.Model):
	nombre_noticia=models.CharField(max_length=200)
	descripcion_noticia=models.TextField()
	fecha_noticia=models.DateField()
	entrenador=models.ForeignKey(Persona, related_name='Entrenador', limit_choices_to={'tipo_persona': 'E'})
	administrador=models.ForeignKey(Persona, related_name='Administrador', limit_choices_to={'tipo_persona': 'A'})

	def __unicode__(self):
		return self.nombre_noticia

	class Meta:
		verbose_name = "Noticia"
		verbose_name_plural = "Noticias"