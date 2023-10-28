from django.contrib import admin
from .models import Bibliotego, Gatunki, Autorzy


# Register your models here.


admin.site.register(Bibliotego)
admin.site.register(Autorzy)
admin.site.register(Gatunki)