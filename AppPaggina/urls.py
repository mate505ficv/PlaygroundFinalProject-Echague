from django.urls import path
from . import views
urlpatterns = [
    path('alumno/', views.alumno, name='alumno'),
    path('', views.inicio,name='inicio'),
    path('profesor/', views.profesor, name='profesor'),
    path('curso/', views.cursos, name='curso'),
    path('buscar_curso/', views.buscarCursos, name='BuscarCursos'),

]
