from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Jeśli nie używasz CsrfViewMiddleware, musisz użyć csrf_protect we wszystkich widokach, które używają tagu szablonu csrf_token, a także tych, które akceptują dane POST.
from django.views.decorators.csrf import csrf_protect 

from django import forms
from django.contrib.auth.models import User

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .forms import AddToCartForm


from django.contrib import messages

from django.contrib.auth import logout

from .models import Bibliotego, Gatunki, Books, Cart, CartItem

def index(request):
    zapytanie = Gatunki.objects.all()
    dane = {'kategorie': zapytanie}
    return render(request, 'szablon.html', {'abc': zapytanie})
    # return HttpResponse(gat)

def kategorie (request, id):
    page = request.GET.get('page', 1)

    kategoria_user = get_object_or_404(Gatunki, pk=id)
    kategoria_ksiazki = Books.objects.filter(gatunki = kategoria_user)
    gatunki = Gatunki.objects.all()
    paginator = Paginator(kategoria_ksiazki, 9)
    dane = {'kategoria_user': kategoria_user,
            'kategoria_ksiazki': paginator.page(page),
            'abc': gatunki}
    return render(request, 'kategorie_ksiazki.html', dane)

def produkt (request, id):
    produkt_user = get_object_or_404(Books, pk=id)
    gatunki = Gatunki.objects.all()
    dane = {'produkt_user': produkt_user, 'abc': gatunki}
    return render(request, 'ksiazka.html', dane)

def logowanie (request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('glowna')
        else:
            messages.info(request, 'Nazwa użytkownika lub hasło jest niepoprawne')

    context = {}
    return render(request, 'logowanie.html', context)


def wyloguj(request):
    logout(request)
    return redirect('logowanie')



# Przeniesienia z pliku forms z powodów braku działania połączenia
class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True) 
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

def rejestracja (request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Konto zostało utworzone dla ' + user)

            return redirect('/l')
        else:
            messages.error(request, 'Nazwa użytkownika, e-mail, hasło lub hasło2 jest niepoprawne')

    context = {'form':form}
    # messages.info(request, 'Nazwa użytkownika, e-mail, hasło lub hasło2 jest niepoprawne')
    return render(request, 'rejestracja.html', context)
        # Create your views here.


def wyszukiwanie(request):
    query = request.GET.get('Search')
    page = request.GET.get('page', 1)
    if query:
        try:
            # Jeśli się udało, wyszukaj po id
            wyniki = Books.objects.filter(book_title__icontains=query)
        except ValueError:
            # Jeśli nie udało się przekształcić na liczbę, wyszukaj po nazwie
            wyniki = Books.objects.all()
    else:
        # Jeśli zapytanie nie zostało podane, zwróć wszystkie książki
        wyniki = Books.objects.all()
    paginator = Paginator(wyniki, 9)
    gatunki = Gatunki.objects.all()
    return render(request, 'kategorie_ksiazki.html', {'kategoria_ksiazki': paginator.page(page),'abc': gatunki, 'query': query})



def nav(request):
    return render(request, 'navbar.html')


@login_required
def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    return render(request, 'koszyk.html', {'cart_items': cart_items})

@login_required
def add_to_cart(request, book_id):
    cart, created = Cart.objects.get_or_create(user=request.user)
    book = get_object_or_404(Books, pk=book_id)

    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)
            cart_item.quantity += quantity
            cart_item.save()
    else:
        form = AddToCartForm()

    return redirect('cart')

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id)
    cart_item.delete()
    return redirect('cart')


from django.shortcuts import render, redirect
from .models import Cart, CartItem, Books

@login_required
def dodaj_do_koszyka(request):
    if request.method == 'POST':
        produkt_id = request.POST.get('produkt_id')
        if produkt_id:
            ksiazka = Books.objects.get(id=produkt_id)

            # Sprawdź, czy dla tego użytkownika istnieje już rekord w koszyku
            koszyk, created = Cart.objects.get_or_create(user=request.user)
            
            # Sprawdź, czy ta książka już istnieje w koszyku, jeśli tak, zwiększ ilość
            item, item_created = CartItem.objects.get_or_create(cart=koszyk, book=ksiazka)
            if not item_created:
                item.quantity += 1
                item.save()

            return redirect('/', produkt_id=produkt_id)
    
    # Jeśli coś poszło nie tak
    return redirect('/')




















# def koszyk(request):
#     return render(request, 'koszyk.html')

# def ksiazka_detail(request, ksiazka_id):
#     ksiazka = get_object_or_404(Bibliotego, id=ksiazka_id)
#     return render(request, 'ksiazka.html', {'produkt_user': ksiazka})

# @login_required
# def dodaj_do_koszyka(request, ksiazka_id):
#     ksiazka = get_object_or_404(Bibliotego, id=ksiazka_id)
#     koszyk, created = Bibliotego.objects.get_or_create(user=request.user)
#     koszyk.ksiazki.add(ksiazka)
#     return JsonResponse({'status': 'Dodano do koszyka'})

# @login_required
# def koszyk(request):
#     koszyk, created = Bibliotego.objects.get_or_create(user=request.user)
#     ksiazki = koszyk.ksiazki.all()
#     return render(request, 'koszyk.html', {'ksiazki': ksiazki, 'koszyk': koszyk})


        