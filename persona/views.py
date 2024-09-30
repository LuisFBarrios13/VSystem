from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Persona

def get_estudiantes(request):
    
    estudiantes = Persona.objects.filter(rol='Estudiante') 
    
    return render(request, 'lista-estudiantes.html',{
        'title': 'Lista de estudiantes ',
        'estudiantes': estudiantes
    })

def lista_personas(request):
    personas = Persona.objects.prefetch_related('cursos').filter(rol='estudiante')
    return render(request, 'persona/lista-estudiantes.html', {'personas': personas})