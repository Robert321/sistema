from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Carrera)
admin.site.register(Estudiante)
admin.site.register(Docente)
admin.site.register(Materia)
admin.site.register(rel_estudiante_materia)
admin.site.register(Notas)