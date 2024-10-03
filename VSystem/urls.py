
from django.contrib import admin
from django.urls import path
from mainApp.views import inicio, get_prueba
from persona.views import get_estudiantes, registrar_persona
from curso.views import getCursos


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('lista-estudiantes/', get_estudiantes, name='lista-estudiantes'),
    path('prueba/', get_prueba, name='prueba'),
    path('cursos/', getCursos, name='get_cursos'),
    path('lista-cursos/', getCursos, name='lista-cursos'),
    path('registrarPersona/', registrar_persona),
]
