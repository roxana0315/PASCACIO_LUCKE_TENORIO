from django.shortcuts import render
from django.http import HttpResponse

def cursos(request):
    return render(request, 'cursos.html', {})

def crear_curso(request):
    return render(request, 'crear_curso.html', {})

def carreras(request):
    return render(request, 'carreras.html', {})

def crear_carrera(request):
    return render(request, 'crear_carrera.html', {})
