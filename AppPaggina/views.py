from django.shortcuts import render, redirect
# Create your views here.
from django.shortcuts import render, redirect
from .forms import Alumno_forms, Profesor_forms, Curso_forms, UsuSearchForm
from .models import Curso
# Create your views here.


def alumno(request):
    if request.method == 'POST':
        alumno_formulario = Alumno_forms(request.POST)
        
        if alumno_formulario.is_valid:
            alumno_formulario.save()
            
            return redirect('/AppPaggina/')
    else:
        alumno_formulario = Alumno_forms()

    return render(request, 'alumno.html',{"alumno_formulario": alumno_formulario})

def profesor(request):
    if request.method == 'POST':
        profesor_formulario = Profesor_forms(request.POST)
        
        if profesor_formulario.is_valid:
            profesor_formulario.save()
            
            return redirect('/AppPagina/')
    else:
        profesor_formulario = Profesor_forms()
    
    
    return render(request,'profesor.html',{"profesor_formulario":profesor_formulario})

def cursos(request):
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
    cursos = []
    form = UsuSearchForm(request.GET)

    if form.is_valid():
        nombre = form.cleaned_data.get('nombre')

        # Realizar la búsqueda en el modelo Curso por nombre
        if nombre:
            cursos= Curso.objects.filter(nombre__icontains=nombre)

    return render(request, 'buscarcurso.html', {'form': form, 'cursos': cursos})