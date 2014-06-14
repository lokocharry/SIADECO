# Create your views here.
# -*- encoding: utf-8 -*-
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from usuarios.forms import *
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required

error='Error al guardar, verifique la información.'

def index(request):
	return render_to_response('index.html', context_instance=RequestContext(request))

def log_in(request):
	if request.method=='POST':
		form=AuthenticationForm(request.POST)
		for field in form.fields:
			form.fields[field].widget.attrs['class'] = 'form-control'
			form.fields[field].widget.attrs['placeholder'] = field
		if form.is_valid:
			usuario=request.POST['username']
			clave=request.POST['password']
			acceso=authenticate(username=usuario, password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect('/verNoticias')
				else:
					error='El usuario no se encuentra activo. Contacte al administrador para corregir el problema'
					return render_to_response('login.html',{'error':error, 'form':form}, context_instance=RequestContext(request))
			else:
				error='El usuario y contraseña no coinciden. Intente nuevamente'
				return render_to_response('login.html', {'error':error, 'form':form}, context_instance=RequestContext(request))		
	else:
		form=AuthenticationForm(request.POST)
		for field in form.fields:
			form.fields[field].widget.attrs['class'] = 'form-control'
			form.fields[field].widget.attrs['placeholder'] = field
	return render_to_response('login.html', {'form':form}, context_instance=RequestContext(request))

@login_required(login_url='/')
def log_out(request):
	logout(request)
	return HttpResponseRedirect('/home')

def about(request):
	return render_to_response('about.html', context_instance=RequestContext(request))

def nuevo_deportista(request):
	form=DeportistaForm()
	if request.method=='POST':
		form=DeportistaForm(request.POST)
		if form.is_valid():
			deportista=form.save()
			deportista.tipo_persona='D'
			userName=deportista.nombre+'.'+deportista.apellido
			eMail=deportista.email
			passw=deportista.telefono
			deportista.usuario=User.objects.create_user(username=userName,email=eMail,password=passw)
			deportista.save()
			g = Group.objects.get(name='Deportistas')
			if g is not None:
				g.user_set.add(deportista.usuario)
			return HttpResponseRedirect('/persona/list')
		return render_to_response('crearUsuario.html', {'form':form, 'error':error}, context_instance=RequestContext(request))
	else:
		form=DeportistaForm()
	return render_to_response('crearUsuario.html',{'form':form, 'accion':'create'}, context_instance=RequestContext(request))

def nuevo_entrenador(request):
	form=EntrenadorForm()
	if request.method=='POST':
		form=EntrenadorForm(request.POST)
		if form.is_valid():
			entrenador=form.save()
			entrenador.tipo_persona='E'
			userName=entrenador.nombre+'.'+entrenador.apellido
			eMail=entrenador.email
			passw=entrenador.telefono
			entrenador.usuario=User.objects.create_user(username=userName,email=eMail,password=passw)
			entrenador.save()
			g = Group.objects.get(name='Entrenadores')
			if g is not None:
				g.user_set.add(entrenador.usuario)
			return HttpResponseRedirect('/persona/list')
		else:
			return render_to_response('crearUsuario.html', {'form':form, 'error':error}, context_instance=RequestContext(request))
	else:
		form=EntrenadorForm()
	return render_to_response('crearUsuario.html',{'form':form, 'accion':'create'}, context_instance=RequestContext(request))

def nuevo_administrador(request):
	form=AdministradorForm()
	if request.method=='POST':
		form=AdministradorForm(request.POST)
		if form.is_valid():
			administrador=form.save()
			administrador.tipo_persona='A'
			userName=administrador.nombre+'.'+administrador.apellido
			eMail=administrador.email
			passw=administrador.telefono
			administrador.usuario=User.objects.create_superuser(username=userName,email=eMail,password=passw)
			administrador.save()
			print administrador.usuario
			g = Group.objects.get(name='Administradores')
			if g is not None:
				g.user_set.add(administrador.usuario)
			return HttpResponseRedirect('/persona/list')
		else:
			return render_to_response('crearUsuario.html', {'form':form, 'error':error}, context_instance=RequestContext(request))

	else:
		form=AdministradorForm()
	return render_to_response('crearUsuario.html',{'form':form, 'accion':'create'}, context_instance=RequestContext(request))