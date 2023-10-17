from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Bibliotego
from .models import Gatunki



def index(request):
    zapytanie = Gatunki.objects.all()
    dane = {'kategorie': zapytanie}
    return render(request, 'szablon.html', {'abc': zapytanie})
    # return HttpResponse(gat)

def kategorie (request, id):
    kategoria_user = get_object_or_404(Gatunki, pk=id)
    kategoria_ksiazki = Bibliotego.objects.filter(Gatunki = kategoria_user)
    gatunki = Gatunki.objects.all()
    dane = {'kategoria_user': kategoria_user,
            'kategoria_ksiazki': kategoria_ksiazki,
            'abc': gatunki}
    return render(request, 'kategorie_ksiazki.html', dane)

def produkt (request, id):
    produkt_user = get_object_or_404(Bibliotego, pk=id)
    gatunki = Gatunki.objects.all()
    dane = {'produkt_user': produkt_user, 'abc': gatunki}
    return render(request, 'ksiazka.html', dane)

def logowanie (request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        messages.info(request, 'Usedsadrname OR')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('glowna')
        else:
            messages.info(request, 'Username OR')

    context = {}
    return render(request, 'logowanie.html', context)

def rejestracja (request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()


    context = {'form':form}
    return render(request, 'rejestracja.html', context)
        # Create your views here.

        