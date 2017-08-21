from django.contrib import admin

# Register your models here.
from .models import Interest, Adres, Person

admin.site.register(Interest)
admin.site.register(Adres)
admin.site.register(Person)