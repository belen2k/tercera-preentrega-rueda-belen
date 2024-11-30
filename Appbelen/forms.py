from django import forms
from models import Profesor, Nota, Estudiante

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'email']

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['nombre', 'codigo', 'profesor']  

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'email', 'Nota']