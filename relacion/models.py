from django.db import models
from persona.models import Persona
from curso.models import Curso

class Relacion(models.Model):
    estudiante = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True, 
    related_name='cursos', limit_choices_to={'rol': 'Estudiante'})
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True)
    fechaInicio = models.DateField()
    fechaFinal = models.DateField()
    estado = models.CharField(max_length=100)
    notaFinal = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return f'{self.estudiante.nombre} - {self.estudiante.apellido} - Curso: {self.curso.nombre}'
    
    class Meta:
        db_table = 'Estudiante_Cursos'
