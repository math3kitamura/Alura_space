from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Galeria</h1><p>Bem-vindo à galeria!</p>')