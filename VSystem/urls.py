from django.contrib import admin
from django.urls import path
from mainApp.views import inicio
from persona.views import get_estudiantes, registrar_persona
from curso.views import getCursos, inscribir_curso
from relacion.views import getRelacion, relacionar_curso_est


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('lista-estudiantes/', get_estudiantes, name='lista-estudiantes'),
    path('cursos/', getCursos, name='get_cursos'),
    path('lista-cursos/', getCursos, name='lista-cursos'),
    path('registrarPersona/', registrar_persona),
    path('inscribirCurso/', inscribir_curso, name='inscribirCurso'),
    path('relacionar_curso_est/', relacionar_curso_est, name='relacionar_curso_est'),
    path('lista-relacion/', getRelacion, name='lista-relacion')
]
