from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse


from persona.models import Persona  
from curso.models import Curso
from .models import Relacion
from .forms import RelacionForm


def getRelacion(request):
    relaciones = Relacion.objects.all()
    estudiantes = Persona.objects.filter(rol='Estudiante')
    cursos = Curso.objects.all()
    return render(request, 'relacion.html', {
        'title': 'Relación estudiantes y curso',
        'relaciones': relaciones,
        'estudiantes' : estudiantes,
        'cursos' : cursos
        
    })
    
def relacion(request):
    data = {
        'form': RelacionForm()
    }
    return render(request, 'relacion.html', data) 

def registrar_relacion(request):
    nombre = request.POST.get()


def relacionar_curso_est(request):
    if request.method == 'POST':
        estudiante_id = request.POST.get('estudiante')
        curso_id = request.POST.get('txtcurso')
        fechaInicio = request.POST.get('fechainicio')
        fechaFinal = request.POST.get('fechafinal')
        estado = request.POST.get('txtestado')
        notaFinal = request.POST.get('notafinal')

        relacion = Relacion(
            estudiante_id=estudiante_id, 
            curso_id=curso_id, 
            fechaInicio=fechaInicio, 
            fechaFinal=fechaFinal, 
            estado=estado, 
            notaFinal=notaFinal
        )
        
        relacion.save()
        return redirect('lista-relacion')
