from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def space(request):
    return render(request, 'main/space.html')

def games(request):
    return render(request, 'main/games.html')


def about(request):
    return render(request, 'main/about.html')
