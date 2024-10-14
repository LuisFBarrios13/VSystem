from django import forms
from .models import Relacion, Persona, Curso

class RelacionForm(forms.ModelForm):
    class Meta:
        model = Relacion
        fields = ['estudiante', 'curso', 'fechaInicio', 'fechaFinal', 'estado', 'notaFinal']
        
    def __init__(self, *args, **kwargs):
        super(RelacionForm, self).__init__(*args, **kwargs)
        self.fields['estudiante'].queryset = Persona.objects.filter(rol='Estudiante')
        
        self.fields['curso'].queryset = Curso.objects.all()
        
        