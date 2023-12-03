from django.urls import path
from .views import cursos, crear_curso, carreras, crear_carrera

urlpatterns = [
    path('cursos/', cursos, name='cursos'),
    path('crear_curso/', crear_curso, name='crear_curso'),
    path('carreras/', carreras, name='carreras'),
    path('crear_carrera/', crear_carrera, name='crear_carrera'),
]
