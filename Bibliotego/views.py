from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from .models import Bibliotego
from .models import Gatunki


def index(request):
    zapytanie = Gatunki.objects.all()
    dane = {'kategorie': zapytanie}
    dane1 = [i for i in zapytanie]
    dane2 ={'zapytanie': zapytanie}
    jeden = Bibliotego.objects.get(pk=1)   # wyszukiwanie na podstawie id obiektu w bibliotece
    gat = Bibliotego.objects.filter(Gatunki=1)  # filtrowanie na podstawie id gatunktów
    # autor = Bibliotego.objects.filter(Autorzy=1)  # filtrowani na podstawie autorwów po id autorów
    gat_name1 = Gatunki.objects.get(id=1)  # filtrowanie na podstawie gatunku i wypisanie gatunku
    gat_name2 = Gatunki.objects.get(id=2)  # filtrowanie na podstawie gatunku i wypisanie gatunku
    gat_name3 = Gatunki.objects.get(id=3)  # filtrowanie na podstawie gatunku i wypisanie gatunku
    # null = Bibliotego.objects.filter(Gatunki__isnull=True)
    # zawiera = Bibliotego.objests.filter(opis__icontains='fantasy') # nie działające

    return render(request, 'szablon.html', {'abc': zapytanie})
    # return HttpResponse(gat)

def kategorie (request, id):
    kategorie_user = Gatunki.objects.get(pk=id)
    return HttpResponse(kategorie_user.nazwa)

def produkt (request, id):
    produkt_user = Bibliotego.objects.get(pk=id)
    gatunki = Gatunki.objects.all()
    dane = {'produkt_user': produkt_user, 'gatunki': gatunki}
    return render(request, 'ksiazka.html', dane)

def logowanie (request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/1')
        else:
            message.info(request, 'Username OR')

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
