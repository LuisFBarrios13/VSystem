from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from .models import Persona
from .forms import PersonaForm

def persona(request):
    data = {
        'form': PersonaForm()
    }
    return render(request, 'lista-estudiantes.html', data)

def get_estudiantes(request):
    
    estudiantes = Persona.objects.filter(rol='Estudiante') 
    
    return render(request, 'lista-estudiantes.html',{
        'title': 'Lista de estudiantes ',
        'estudiantes': estudiantes
    })

def lista_personas(request):
    personas = Persona.objects.prefetch_related('cursos').filter(rol='estudiante')
    return render(request, 'persona/lista-estudiantes.html', {'personas': personas})

def registrar_persona(request):
        nombre = request.POST.get('txtnombre')
        apellido = request.POST.get('txtapellido') 
        dni = request.POST.get('numdni')  
        telefono = request.POST.get('numtelefono')
        correo = request.POST.get('correo')  
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        rol = 'Estudiante'
        
        peronas = Persona.objects.create(
            nombre = nombre,
            apellido = apellido,
            dni = dni,
            telefono = telefono,
            correo = correo,
            fecha_nacimiento = fecha_nacimiento,
            rol = rol
        )
        
        return redirect('lista-estudiantes')