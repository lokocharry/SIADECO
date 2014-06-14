from django import forms
from usuarios.models import Persona

class DeportistaForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(DeportistaForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'
			self.fields[field].widget.attrs['placeholder'] = field
			
	class Meta:
		model=Persona
		exclude = ['cargo_colegio', 'titulo', 'tipo_persona', 'usuario']

class AdministradorForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(AdministradorForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'
			self.fields[field].widget.attrs['placeholder'] = field
			
	class Meta:
		model=Persona
		exclude = ['modalidad', 'grado', 'titulo', 'tipo_persona', 'usuario']

class EntrenadorForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(EntrenadorForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'
			self.fields[field].widget.attrs['placeholder'] = field
			
	class Meta:
		model=Persona
		exclude = ['modalidad', 'grado', 'cargo_colegio', 'tipo_persona', 'usuario']