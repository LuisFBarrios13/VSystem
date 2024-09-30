from django.shortcuts import render
from .models import Curso

def inicio(request):
    return render(request, 'index.html');

def get_prueba(request):
    return render(request, 'prueba.html');

def get_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'mainApp/cursos.html', {'cursos': cursos});

def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/lista.html', {'cursos': cursos});