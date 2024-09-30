from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Curso

def getCursos(request):
    
    cursos = Curso.objects.all()
    return render(request, 'cursos.html', {
        'tittle': 'Listado de Cursos',
        'cursos' : cursos
    })
    
    
