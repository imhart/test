
from django.db import models
from django.contrib.auth.models import User

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
    zdjęcie = models.ImageField(null=True, blank=True, upload_to="images/")  # Pole do dodawania zdjęć

    # Tworzenie nazwy do pojedyńczej i mnogiej do książek w bibliotece
    class Meta:
        verbose_name = "Książka1"
        verbose_name_plural = "Książki1"


class Books(models.Model):
    def __str__(self):
        return self.book_title
    isbn = models.CharField(db_column='ISBN', max_length=255,blank=True, null=True)  # Field name made lowercase.
    gatunki = models.ForeignKey(Gatunki, null=True, blank=True, on_delete=models.CASCADE,)
    book_title = models.CharField(db_column='Book-Title', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    book_author = models.CharField(db_column='Book-Author', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    year_of_publication = models.IntegerField(db_column='Year-Of-Publication', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    publisher = models.CharField(db_column='Publisher', max_length=255,  blank=True, null=True)  # Field name made lowercase.
    image_url_s = models.CharField(db_column='Image-URL-S', max_length=255,  blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    image_url_m = models.CharField(db_column='Image-URL-M', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    image_url_l = models.CharField(db_column='Image-URL-L', max_length=255,  blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        db_table = 'books'
        verbose_name = "Książka2"
        verbose_name_plural = "Książki2"



class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Books, through='CartItem')

class CartItem(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_item_total(self):
        return 2 * self.quantity
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    koszyk = models.ManyToManyField(Books, blank=True)


# class Koszyk(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     ksiazki = models.ManyToManyField(Bibliotego)



