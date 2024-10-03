from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'capacidadMaxima', 'profesor']

    def clean_profesor(self):
        profesor = self.cleaned_data.get('profesor')

        # Verificar si se ha asignado un profesor antes de acceder al rol
        if profesor is not None:
            if profesor.rol == 'Estudiante':  # Verifica si el rol es 'Estudiante'
                raise forms.ValidationError('No puedes asignar a un estudiante como profesor.')
        
        # Si profesor es None, devolver None o el valor actual sin validar
        return profesor