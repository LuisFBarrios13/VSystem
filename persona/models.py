from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=10)
    telefono = models.CharField(max_length=10)
    correo = models.EmailField()
    fecha_nacimiento = models.DateField()
    rol = models.CharField(max_length=20)
    create_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.dni} - {self.rol}'

    class Meta:
        db_table = 'Persona'
