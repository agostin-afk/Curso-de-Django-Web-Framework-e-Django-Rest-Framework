from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    context = {'name': 'Agosto'}
    return render(request, 'recipes/pages/home.html', context)


def contato(request):
    return render(request, 'contato.html')


def sobre(request):
    return render(request, 'sobre.html')
