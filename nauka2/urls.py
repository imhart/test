"""nauka2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Bibliotego.views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='glowna'),
    path('kategorie/<id>/', kategorie, name='kategorie'),
    path('produkt/<id>/', produkt, name='produkt'),
    path('l', logowanie, name='logowanie'),
    path('w', wyloguj, name='wyloguj'),
    path('r', rejestracja, name='rejestracja'),
    path('nav', nav, name='nav'), 
    path('wyszukiwanie', wyszukiwanie, name='wyszukiwanie'),

    path('cart', cart, name='cart'),
    path('add-to-cart/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),


    # path('ksiazka/<int:ksiazka_id>/', ksiazka_detail, name='ksiazka_detail'),
    path('dodaj_do_koszyka', dodaj_do_koszyka, name='dodaj_do_koszyka'),
    # Dodaj inne url'e
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)