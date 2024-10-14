from django import forms
from .models import Matricula

class MatriculaForm(forms.ModelForm):
    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Suspendido', 'Suspendido'),
        ('Finalizado', 'Finalizado'),
    ]

    estado = forms.ChoiceField(choices=ESTADO_CHOICES)

    class Meta:
        model = Matricula
        fields = ['estado', 'fechaInicio', 'costo', 'relacion']  