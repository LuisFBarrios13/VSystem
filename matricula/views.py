from django.shortcuts import render, redirect
from relacion.models import Relacion 
from .models import Matricula
from .forms import MatriculaForm

def getMatricula(request):
    matriculas = Matricula.objects.all()
    relaciones = Relacion.objects.all()
    return render(request, 'matriculas.html', {
        'title': 'Lista de Matrículas',
        'matriculas': matriculas,
        'relaciones': relaciones
    })
    
def matricula(request):
    data = {
        'form' : MatriculaForm()
    }
    return render(request, 'matriculas.html', data)
    
def registrar_matricula(request):
    if request.method == 'POST':
        relacion_id = request.POST.get('htrelacion')
        fechaInicio = request.POST.get('htfechaInicio')
        estado = request.POST.get('htestado')
        costo = request.POST.get('htcosto')
        
        matricula = Matricula(
            relacion_id=relacion_id,
            fechaInicio=fechaInicio,
            estado=estado,
            costo=costo,
        )
        
        matricula.save()
        return redirect('lista-matricula')


    
