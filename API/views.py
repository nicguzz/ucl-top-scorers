from django.shortcuts import render, redirect
from .foot import top_scorers


def home(request):
    return render(request, 'home.html')


def topscorers(request):

    return render(request, 'topscorers.html', {'top_scorers': top_scorers})
