from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("<h1>PostaFacil<h1>")

def cadastro(request):
    return render(request, "postafacil/cadastro.html")