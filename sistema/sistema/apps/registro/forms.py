from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User


class CarreraForm(ModelForm):
	nombre	= forms.CharField(label="Nombre de Carrera",widget=forms.TextInput())
	direccion	= forms.CharField(label="La Direccion",widget=forms.TextInput())
	telefono	= forms.CharField(label="El Telefono",widget=forms.TextInput())
	catidadsemestres=forms.IntegerField(label="Los Semestres",widget=forms.TextInput())
	class Meta:
		model=Carrera
		fields=["nombre","direccion","telefono","catidadsemestres"] 

class ContactForm(ModelForm):
	class Meta:
		model=Carrera
		fields=["nombre","direccion","telefono"] 


class LoginEstudianteForm(forms.Form):
	email = forms.EmailField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))

class RegistrarEstudiante(ModelForm):
	nombre=forms.CharField(error_messages={"required":"El nombre esta vacio"})
	apellido=forms.CharField(error_messages={"required":"El apellido esta vacio"})
	ci=forms.CharField(error_messages={"required":"El ci esta vacio"})
	email=forms.EmailField(error_messages={"required":"El email esta vacio"})

	class Meta:
		model=Estudiante
		fields=["nombre","apellido","ci","email"] 

class Registro_Estudiante(ModelForm):
	class Meta():
		model=Estudiante
		fields=["nombre","apellido","ci","email","password"]

class Registro_Docente(ModelForm):
	class Meta():
		model=Docente
		fields=["nombre","apellido","ci","email","password"]



class RegistrarDocente(ModelForm):
	nombre=forms.CharField(error_messages={"required":"El nombre esta vacio"})
	apellido=forms.CharField(error_messages={"required":"El apellido esta vacio"})
	ci=forms.CharField(error_messages={"required":"El ci esta vacio"})
	email=forms.EmailField(error_messages={"required":"El email esta vacio"})
	class Meta:
		model=Docente
		fields=["nombre","apellido","ci","email"] 

class RegistrarMateria(forms.ModelForm):
	class Meta():
		model=Materia
class RegistrarRelEstMat(forms.ModelForm):
	class Meta():
		model=rel_estudiante_materia
class RegistrarNotas(forms.ModelForm):
	class Meta():
		model=Notas