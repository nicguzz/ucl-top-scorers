from django.shortcuts import render, redirect
from requests import get
from .foot import get_top_scorers


def home(request):
    return render(request, 'home.html')


def topscorers(request):

    return render(request, 'topscorers.html', {'top_scorers': get_top_scorers()})
