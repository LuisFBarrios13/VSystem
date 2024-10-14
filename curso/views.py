from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse

from persona.models import Persona
from .models import Curso
from .forms import CursoForm

def getCursos(request):
    cursos = Curso.objects.all()
    profesores = Persona.objects.filter(rol='Docente')
    return render(request, 'cursos.html', {
        'title': 'Listado de Cursos',
        'cursos': cursos,
        'profesores': profesores  
    })
    
def curso(request):
    data = {
        'form': CursoForm()
    }
    return render(request, 'cursos.html', data)

def registrar_curso(request):
    nombre = request.POST.get()
    
def inscribir_curso(request):
    if request.method == 'POST':
        nombre = request.POST.get('txtnombre')
        capacidad_maxima = request.POST.get('txtcapacidadmaxima')
        profesor_id = request.POST.get('profesor')

        curso = Curso(nombre=nombre, capacidadMaxima=capacidad_maxima, profesor_id=profesor_id)
        curso.save()
        return redirect('get_cursos')
    
    profesores = Persona.objects.filter(rol='Docente')
    
    return render(request, 'cursos.html', {'profesores': profesores})
    
    
