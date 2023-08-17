from django.urls import path
from . import views
app_name = 'AppPaggina'
urlpatterns = [
    path('alumno/', views.alumno, name='alumno'),
    path('', views.inicio,name='inicio'),
    path('profesor/', views.profesor, name='profesor'),
    path('curso/', views.cursos, name='curso'),
    path('buscar_curso/', views.buscarCursos, name='BuscarCursos'),
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
]
