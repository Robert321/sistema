from django.db import models
from django import forms
from django.contrib.auth.models import User

	
class Estudiante(models.Model):
	nombre=models.CharField(max_length=150)
	apellido=models.CharField(max_length=150)
	ci=models.CharField(max_length=20)
	email=models.EmailField()
	password=models.CharField(max_length=150)
	fecha=models.DateField()
	hora=models.TimeField()
	def __unicode__(self):
		return self.nombre

class Docente(models.Model):
	nombre=models.CharField(max_length=150)
	apellido=models.CharField(max_length=150)
	ci=models.CharField(max_length=20)
	email=models.EmailField()
	password=models.CharField(max_length=150)
	fecha=models.DateField()
	hora=models.TimeField()
	def __unicode__(self):
		return self.nombre

#carrera
class Carrera(models.Model):
	nombre=models.CharField(max_length=200)
	direccion=models.CharField(max_length=200)
	telefono=models.CharField(max_length=200)
	catidadsemestres=models.IntegerField()
	def __unicode__(self):
		return self.nombre


class Materia(models.Model):
	nombre=models.CharField(max_length=150)
	sigla=models.CharField(max_length=150)
	fecha=models.DateField()
	hora=models.TimeField()
	idCar=models.ForeignKey(Carrera)
	def __unicode__(self):
		return self.nombre

class rel_estudiante_materia(models.Model):
	idMateria=models.ForeignKey(Materia)
	idEstudiante=models.ForeignKey(Estudiante)
	def __unicode__(self):
		return"%s Materia %s"%(self.idEstudiante.apellido,self.idMateria.sigla)

class Notas(models.Model):
	nombre=models.CharField(max_length=200)
	descripcion=models.TextField()
	notamin=models.IntegerField()
	notamax=models.IntegerField()
	notamindeaprovacion=models.IntegerField()
	idrelestmat=models.ForeignKey(rel_estudiante_materia)
	def __unicode__(self):
		return self.nombre
