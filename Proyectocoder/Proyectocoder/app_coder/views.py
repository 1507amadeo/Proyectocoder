from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Curso

def curso(self):
    curso = Curso(nombre="python" , camada="1993")
    curso.save()
    documentoDeTexto = f"Curso: {curso.nombre}, Camada: {curso.camada}"


    return HttpResponse(documentoDeTexto)

# Create your views here.
