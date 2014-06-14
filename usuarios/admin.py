from usuarios.models import *
from django.contrib import admin
from usuarios.models import Persona

admin.site.register(Persona)
admin.site.register(EPS)
admin.site.register(FechaEntrenador)

class ArchivoAdmin(admin.ModelAdmin):
	def save_model(self, request, obj, form, change):
		print request.user.id
		obj.persona=Persona.objects.get(usuario=request.user)
		obj.save()

admin.site.register(Archivo, ArchivoAdmin)