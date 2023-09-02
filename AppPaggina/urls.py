from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
app_name = 'AppPaggina'
urlpatterns = [
    path('alumno/', views.alumno, name='alumno'),
    path('', views.inicio,name='inicio'),
    path('profesor/', views.profesor, name='profesor'),
    path('curso/', views.cursos, name='curso'),
    path('buscar_curso/', views.buscarCursos, name='BuscarCursos'),
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', LogoutView.as_view(template_name= 'logout.html'), name='logout'),
    path('tarea/', views.tarea, name='tarea'),
    path('editarperfil/', views.editar_perfil, name="EditarPerfil"),    
    path('cambiarcontrasenia/', views.CambiarContrasenia.as_view(), name="CambiarContrasenia"),
    path('aboutm/', views.aboutm, name="AboutMe")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)