from django.contrib import admin
from .models import Bibliotego, Gatunki, Autorzy, Books


# Register your models here.
# class BooksAdmin(admin.ModelAdmin):
#     list_display = ('__all__',) 


admin.site.register(Bibliotego)
admin.site.register(Autorzy)
admin.site.register(Gatunki)
admin.site.register(Books)
