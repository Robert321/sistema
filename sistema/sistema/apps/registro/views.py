from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
import datetime
# Create your views here.
def index_view(request):
	return render_to_response("index.html",{},RequestContext(request))


def MenuEstudiante(request,id):
	idest=int(id)
	registro=Estudiante.objects.get(id=idest)
	return render_to_response("menuestudiante.html",{"dato":registro},RequestContext(request))


def MenuDocente(request,id):
	iddoc=int(id)
	registro=Docente.objects.get(id=iddoc)
	return render_to_response("menudocente.html",{"dato":registro},RequestContext(request))

def login_view_Estudiante(request):
	pdb.set_trace()
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == "POST":
			form = LoginEstudianteForm(request.POST)
			if form.is_valid():
				next = request.POST['next']
				email = form.cleaned_data['email']
				password = form.cleaned_data['password']
				usuario = authenticate(email=email,password=password)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return HttpResponseRedirect(next)
				else:
					mensaje = "Es y/o password incorrecto"
		next = request.REQUEST.get('next')
		form = LoginEstudianteForm()
		ctx = {'form':form,'mensaje':mensaje,'next':next}
		return render_to_response('LoginEstudiante.html',ctx,context_instance=RequestContext(request))

def addEstudiante(request):
	if request.method=="POST":
		formulario=RegistrarEstudiante(request.POST)
		if formulario.is_valid():
			p=Estudiante(
				nombre=formulario.cleaned_data["nombre"],
				apellido=formulario.cleaned_data["apellido"],
				ci=formulario.cleaned_data["ci"],
				email=formulario.cleaned_data["email"],
				password=formulario.cleaned_data["nombre"]+formulario.cleaned_data["ci"],
				fecha=datetime.datetime.now().date(),
				hora=datetime.datetime.now().time(),
				)
			p.save()
			url=str(p.id)
			return HttpResponseRedirect("/menuestudiante/"+url+"/")
	else:
		formulario=RegistrarEstudiante()
	return render_to_response("estudiante.html",{"form":formulario},RequestContext(request))



def editar_estudiante(request, id):
    elid=int(id)
    consulta=Estudiante.objects.get(id=elid)
    if request.method =="POST":
        form=Registro_Estudiante(request.POST,request.FILES)
        if form.is_valid():
            nombre=form.cleaned_data["nombre"]
            apellido=form.cleaned_data["apellido"]
            ci=form.cleaned_data["ci"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            consulta.nombre=nombre
            consulta.apellido=apellido
            consulta.ci=ci
            consulta.email=email
            consulta.password=password
            consulta.save()
            return HttpResponseRedirect("/menuestudiante/")
    if request.method == "GET":
        form=Registro_Estudiante(initial={
                'nombre':consulta.nombre,
                'apellido':consulta.apellido,
                'ci':consulta.ci,
                'email':consulta.email,
                'password':consulta.password,
            })
    ctx={"form":form,"persona":consulta}
    return render_to_response("modificarestudiante.html",ctx,RequestContext(request))




def logout_view_Estudiante(request):
	logout(request)
	return HttpResponseRedirect('/')


def addDocente(request):
	if request.method=="POST":
		formulario=RegistrarDocente(request.POST)
		if formulario.is_valid():
			p=Docente(
				nombre=formulario.cleaned_data["nombre"],
				apellido=formulario.cleaned_data["apellido"],
				ci=formulario.cleaned_data["ci"],
				email=formulario.cleaned_data["email"],
				password=formulario.cleaned_data["nombre"]+formulario.cleaned_data["ci"],
				fecha=datetime.datetime.now().date(),
				hora=datetime.datetime.now().time(),
				)
			p.save()
			url=str(p.id)
			return HttpResponseRedirect("/menudocente/"+url+"/")
	else:
		formulario=RegistrarDocente()
	return render_to_response("docente.html",{"form":formulario},RequestContext(request))


def editar_docente(request, id):
    elid=int(id)
    consulta=Docente.objects.get(id=elid)
    if request.method =="POST":
        form=Registro_Docente(request.POST,request.FILES)
        if form.is_valid():
            nombre=form.cleaned_data["nombre"]
            apellido=form.cleaned_data["apellido"]
            ci=form.cleaned_data["ci"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            consulta.nombre=nombre
            consulta.apellido=apellido
            consulta.ci=ci
            consulta.email=email
            consulta.password=password
            consulta.save()
            return HttpResponseRedirect("/menudocente/")
    if request.method == "GET":
        form=Registro_Docente(initial={
                'nombre':consulta.nombre,
                'apellido':consulta.apellido,
                'ci':consulta.ci,
                'email':consulta.email,
                'password':consulta.password,
            })
    ctx={"form":form,"persona":consulta}
    return render_to_response("modificardocente.html",ctx,RequestContext(request))





def exito(request):
	return render_to_response("exito.html",{},RequestContext(request))


def addCarrera(request):
	if request.method == "POST":
		formulario = CarreraForm(request.POST)
		if formulario.is_valid():
			p=Carrera(
				nombre = formulario.cleaned_data["nombre"],
				direccion = formulario.cleaned_data["direccion"],
				telefono = formulario.cleaned_data["telefono"],
				catidadsemestres=formulario.cleaned_data["catidadsemestres"],
			)
			p.save()
			return HttpResponseRedirect("/registro/exito/")
	else:
		formulario = CarreraForm()
	return render_to_response("carrera.html",{"form":formulario},RequestContext(request))

def VerContacto(request):
	lista=Carrera.objects.all()
	return render_to_response("vercontacto.html",{"dato":lista},RequestContext(request))

def addMateria(request):
	formulario=RegistrarMateria()
	return render_to_response("materia.html",{"form":formulario},RequestContext(request))
def addRelEstMat(request):
	formulario=RegistrarRelEstMat()
	return render_to_response("programacion.html",{"form":formulario},RequestContext(request))
def addNotas(request):
	formulario=RegistrarNotas()
	return render_to_response("notas.html",{"form":formulario},RequestContext(request))