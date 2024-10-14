from django.contrib import admin
from django.contrib import admin
from .models import Relacion

@admin.register(Relacion)
class EstudianteCursoAdmin(admin.ModelAdmin):
    list_display = ("estudiante", "curso", "fechaInicio", "fechaFinal", "estado", "notaFinal")
