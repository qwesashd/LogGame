from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy



def index(request):
    return render(request, 'main/index.html')

def login(request):
    return render(request, 'main/login.html')

def reg(request):
    return render(request, 'main/reg.html')

def error(request):
    return render(request, 'main/error.html')

def space(request):
    return render(request, 'main/space.html')

def games(request):
    return render(request, 'main/games.html')

def send(request):
    return render(request, 'main/send.html')


def about(request):
    return render(request, 'main/about.html')


def support(request):
    return render(request, 'main/support.html')



