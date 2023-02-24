from django.forms import ModelForm
from django import forms
from .models import Usuario

#class UsuarioForm(forms.ModelForm):
#    class Meta:
#        model = Usuario
#        fields = ['nombre', 'correo']

class UsuarioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus']=True
    
    class Meta:
        model=Usuario
        fields='__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su Nombre', 'type':'text'}),
            'correo': forms.TextInput(attrs={'class':'form-control mt-2', 'placeholder':'Ingrese su Correo', 'type':'text'}),
        }

