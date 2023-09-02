from django import forms
from .models import Alumno, Profesor, Curso
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class Alumno_forms(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'

class Profesor_forms(forms.ModelForm):
    class Meta:
        model = Profesor
        fields ='__all__'
        
class aboutMe_forms(forms.ModelForm):
    print("Hola")

class Curso_forms(forms.ModelForm):
    class Meta:
        model = Curso
        fields  ='__all__'
class UserEditForm(forms.ModelForm):
    password = None
    email = forms.EmailField()
    class Meta:
        model = User
        fields  =['email', 'password']
class UsuSearchForm(forms.Form):
    nombre = forms.CharField(required=False)

class UserCreationFormCustom(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
