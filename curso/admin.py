from django.contrib import admin
from.models import Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'capacidadMaxima', 'profesor')

# Register your models here.
