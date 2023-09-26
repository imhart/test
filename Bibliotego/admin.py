from django.contrib import admin
from .models import Bibliotego
from .models import Autorzy
from .models import Gatunki


# Register your models here.


admin.site.register(Bibliotego)
admin.site.register(Autorzy)
admin.site.register(Gatunki)