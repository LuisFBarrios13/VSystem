from django.db import models
from relacion.models import Relacion

class Matricula(models.Model):
    
    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Suspendido', 'Suspendido'),
        ('Finalizado', 'Finalizado'),
    ]
    
    relacion = models.ForeignKey(Relacion, on_delete=models.SET_NULL, null=True)
    fechaInicio = models.DateField()
    estado = models.CharField(max_length=150, choices=ESTADO_CHOICES, default='Activo')
    costo = models.DecimalField(max_digits=8, decimal_places=1)
    
    def __str__(self):
        if self.relacion is not None:
            return f'Matrícula de {self.relacion.estudiante.nombre} en {self.relacion.curso.nombre} - Estado: {self.estado} - Costo: {self.costo}'
        return "Matrícula sin relación"
   
    class Meta:
        db_table = 'Matriculas' 




    
