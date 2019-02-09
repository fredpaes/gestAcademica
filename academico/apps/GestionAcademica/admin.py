from django.contrib import admin
from academico.apps.GestionAcademica.models import *

# Register your models here.

admin.site.register(Alumno)
admin.site.register(Curso)
admin.site.register(Matricula)