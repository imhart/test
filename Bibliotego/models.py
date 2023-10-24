
from django.db import models
from django.contrib.auth.models import User

class Venue(models.Model):
    venue_image = models.ImageField(null=True, blank=True, upload_to="images/")
    def __str__(self):
        return self.name

class Autorzy(models.Model):
    def __str__(self):
        return self.nazwa

    nazwa = models.CharField(max_length=60)
    opis = models.TextField(blank=True)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autorzy"


class Gatunki(models.Model):
    def __str__(self):
        return self.nazwa

    nazwa = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Gatunek"
        verbose_name_plural = "Gatunki"

class Bibliotego(models.Model):
    def __str__(self):
        return self.nazwa

    Gatunki = models.ForeignKey(Gatunki, null=True, blank=True, on_delete=models.CASCADE,)
    Autorzy = models.ForeignKey(Autorzy, on_delete=models.CASCADE, null=True)
    nazwa = models.CharField(max_length=100)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=12, decimal_places=2)

    # Tworzenie nazwy do pojedyńczej i mnogiej do książek w bibliotece
class Meta:
        verbose_name = "Książka"
        verbose_name_plural = "Książki"




