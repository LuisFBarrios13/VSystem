from django.db import models
from persona.models import Persona
from django.core.exceptions import ValidationError

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    capacidadMaxima = models.IntegerField(default=30)
    profesor = models.ForeignKey(Persona, on_delete=models.CASCADE, null=True, blank=True)

    
    def clean(self):
        # Validación de capacidad máxima
        if self.capacidadMaxima <= 0:
            raise ValidationError('La capacidad máxima debe ser mayor que cero.')
        
        # Validación de rol de profesor
        if self.profesor.rol != 'Docente':
            raise ValidationError('El rol del profesor debe ser "Docente".')
    
    def __str__(self):
        if self.profesor:
           return f'{self.nombre} - {self.profesor.nombre}'
        else:
            return f'{self.nombre} - Sin Profesor Asignado'
        

    
    class Meta:
        db_table = 'curso'
