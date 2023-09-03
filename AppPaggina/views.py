from django.shortcuts import render, redirect
# Create your views here.
from django.shortcuts import render, redirect
from .forms import Alumno_forms, Profesor_forms, Curso_forms, UsuSearchForm, UserEditForm
from .models import Curso, Tarea
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

# Create your views here

from django.http import HttpResponse

def aboutm(request):
    context = {
    }
    return render(request, 'aboutm.html', context)

class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView, View):
    def get(self, request):
        form = PasswordChangeForm(request.user)
        return render(request, 'cambiarcontrasenia.html', {'form': form})

    def post(self, request):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('/AppPaggina/')
        return render(request, 'cambiarcontrasenia.html', {'form': form})
def editar_perfil(request):
    user = request.user
    if request.method == "POST":   
        miformulario = UserEditForm(request.POST, instance=request.user)

        if miformulario.is_valid():
            miformulario.save()

            return redirect('/AppPaggina/')        
    else:
        miformulario = miformulario = UserEditForm(instance=request.user)
        return render(request, 'editarperfil.html',{"miformulario": miformulario})

def alumno(request):
    if not request.user.is_authenticated:
        return redirect('http://127.0.0.1:8000/AppPaggina/login/')
    if request.method == 'POST':
        alumno_formulario = Alumno_forms(request.POST)
        
        if alumno_formulario.is_valid():
            alumno_formulario.save()
            
            return redirect('/AppPaggina/')
    else:
        alumno_formulario = Alumno_forms()

    return render(request, 'alumno.html',{"alumno_formulario": alumno_formulario})
def profesor(request):
    if not request.user.is_authenticated:
        return redirect('http://127.0.0.1:8000/AppPaggina/login/')
    if request.method == 'POST':
        profesor_formulario = Profesor_forms(request.POST)
        
        if profesor_formulario.is_valid():
            profesor_formulario.save()
            
            return redirect('/AppPagina/')
    else:
        profesor_formulario = Profesor_forms()
    
    
    return render(request,'profesor.html',{"profesor_formulario":profesor_formulario})

def cursos(request):
    if not request.user.is_authenticated:
        return redirect('http://127.0.0.1:8000/AppPaggina/login/')
    if request.method == 'POST':
        cursos_formulario = Curso_forms(request.POST)
        
        if cursos_formulario.is_valid():
            cursos_formulario.save()       
            return redirect('/AppPaggina/')
    else:
        cursos_formulario = Curso_forms()
    
    return render(request, 'curso.html',{"cursos_formulario": cursos_formulario})


def inicio(request):
    return render(request,'inicio.html')

def buscarCursos(request):
    if not request.user.is_authenticated:
        return redirect('http://127.0.0.1:8000/AppPaggina/login/')
    cursos = []
    form = UsuSearchForm(request.GET)

    if form.is_valid():
        nombre = form.cleaned_data.get('nombre')

        # Realizar la búsqueda en el modelo Curso por nombre
        if nombre:
            cursos= Curso.objects.filter(nombre__icontains=nombre)

    return render(request, 'buscarcurso.html', {'form': form, 'cursos': cursos})

def tarea(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        descripcion = request.POST['descripcion']
        archivo = request.FILES['archivo']

        tarea = Tarea.objects.create(
        titulo=titulo,
        descripcion=descripcion,
        archivo=archivo,
        )
        
        
        # Puedes redirigir a donde quieras después de subir la tarea
        return render(request, 'inicio.html')
    else:
        return render(request, 'tarea.html')


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return render(request, 'inicio.html', {"mensaje": "Bienvenido"})
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def register_request(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            contraseña = form.cleaned_data['password1']
            form.save()
            return render(request, "inicio.html", {"mensaje": "Usuario Creado   :)"})
    else:
        form = UserCreationForm()
    
    return render(request, "register.html", {"form": form})
