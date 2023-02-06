from django import forms

class ProfesorFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    materia = forms.CharField(max_length=40)
    fecha_nacimiento = forms.DateField()
    email = forms.EmailField()

class AlumnoFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    materia = forms.CharField(max_length=40)
    fecha_nacimiento = forms.DateField()
    email = forms.EmailField()

class CarreraFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    materias = forms.CharField(max_length=40)

class EntregableFormulario(forms.Form):

    materia = forms.CharField(max_length=40)
    entregado = forms.BooleanField()
