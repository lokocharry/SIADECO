from django.db import models
from django.contrib.auth.models import User
from deportes.models import Modalidad
from django.core.urlresolvers import reverse
from bsct.models import BSCTModelMixin

# Create your models here.

class EPS (BSCTModelMixin, models.Model):
	nombre=models.CharField(max_length=20)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = "EPS"
		verbose_name_plural = "EPS's"

class Persona(BSCTModelMixin, models.Model):
	nombre=models.CharField(max_length=15)
	apellido=models.CharField(max_length=15)
	direccion=models.CharField(max_length=15)
	telefono=models.CharField(max_length=15)
	email=models.EmailField(max_length=75)
	peso=models.IntegerField()
	estatura=models.IntegerField()
	TALLA_ROPA=(
		('S', 'S'),
		('M', 'M'),
		('L', 'L'),
		('X', 'X'),
	)
	talla_ropa=models.CharField(max_length=20, choices=TALLA_ROPA)
	TALLA_CALZADO=(
		('25', '25'),
		('26', '26'),
		('27', '27'),
		('28', '28'),
		('29', '29'),
		('30', '30'),
		('31', '31'),
		('32', '32'),
		('33', '33'),
		('34', '34'),
		('35', '35'),
		('36', '36'),
		('37', '37'),
		('38', '38'),
		('39', '39'),
		('40', '40'),
		('41', '41'),
		('41', '42'),
		('43', '43'),
		('44', '44'),
		('45', '45'),
	)
	talla_calzado=models.CharField(max_length=20, choices=TALLA_CALZADO)
	TIPO_SANGRE=(
		('A+', 'A+'),
		('B+', 'B+'),
		('O+', 'O+'),
		('AB+', 'AB+'),
		('A-', 'A-'),
		('B-', 'B-'),
		('O-', 'O-'),
		('AB-', 'AB-'),
	)
	tipo_sangre=models.CharField(max_length=20, choices=TIPO_SANGRE)
	TIPO_PERSONA=(
		('D', 'Deportista'),
		('A', 'Administrador'),
		('E', 'Entrenador'),
	)
	eps=models.ForeignKey(EPS)
	tipo_persona=models.CharField(max_length=20, choices=TIPO_PERSONA, null=True, blank=True)
	#deportista
	modalidad=models.ForeignKey(Modalidad, null=True, blank=True)
	GRADO=(
		(1, 1),
		(2, 2),
		(3, 3),
		(4, 4),
		(5, 5),
		(6, 6),
		(7, 7),
		(8, 8),
		(9, 9),
		(10, 10),
		(11, 11),
	)
	grado=models.IntegerField(choices=GRADO, null=True, blank=True)
	usuario=models.OneToOneField(User, unique=True, null=True, blank=True)
	#administrador
	cargo_colegio=models.CharField(max_length=40, null=True, blank=True)
	#entranador
	titulo=models.CharField(max_length=40, null=True, blank=True)

	def usuario_detail( self ):
		return '%s' % ( self.usuario )

	def tipo_persona_detail( self ):
		return '%s' % ( self.tipo_persona )

	def __unicode__(self):
		return u'%s %s (%s)' % (self.nombre, self.apellido, self.tipo_persona)

	class Meta:
		verbose_name = "Persona"
		verbose_name_plural = "Personas"

class FechaEntrenador(BSCTModelMixin, models.Model):
	entrenador=models.ForeignKey(Persona, limit_choices_to={'tipo_persona': 'E'})
	fecha_inicio=models.DateField()
	fecha_fin=models.DateField(null=True, blank=True)

	def entrenador_detail( self ):
		return '%s' % ( self.entrenador )

	def fecha_fin_detail( self ):
		if self.fecha_fin is None:
			return 'Aun vinculado'
		else:
			return '%s' % ( self.fecha_fin )

	def __unicode__(self):
		if self.fecha_fin is None:
			return u'%s (Inicio: %s,  Fin: %s)' % (self.entrenador, self.fecha_inicio, 'Aun vinculado')
		else:
			return u'%s (Inicio: %s,  Fin: %s)' % (self.entrenador, self.fecha_inicio, self.fecha_fin)
		

	class Meta:
		verbose_name = "Fecha entrenador"
		verbose_name_plural = "Fechas entrenador"

class Archivo(BSCTModelMixin, models.Model):
	persona=models.ForeignKey(Persona)
	descripcion=models.TextField()
	archivo=models.FileField(upload_to='files', verbose_name='Archivo')

	def save(self):
		print self

	def persona_detail( self ):
		return '%s' % ( self.persona )

	def __unicode__(self):
		return '%s %s' % (self.persona, self.archivo)

	class Meta:
		verbose_name = "Archivo"
		verbose_name_plural = "Archivos"
