from django.contrib import admin
from .models import Opony, Koszyk
# Register your models here.
@admin.register(Opony)
class OponyAdmin(admin.ModelAdmin):
    list_display = ["producent", "zdjecie"]
@admin.register(Koszyk)
class KoszykAdmin(admin.ModelAdmin):
    list_display = ["lista_zakupow"]
