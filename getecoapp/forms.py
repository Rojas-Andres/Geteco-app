from django import forms
from getecoapp.models import Ciudad
class CrearRegistro(forms.Form):
    empresa = forms.CharField(label='Empresa', max_length=100)
    ciudades = Ciudad.objects.all()
    a = [(i.id,i.nombre_ciudad) for i in ciudades]
    CHOICES = tuple(a)
    ciudad = forms.TypedChoiceField(choices=CHOICES, coerce=str)
