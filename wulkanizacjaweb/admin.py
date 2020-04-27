from django.contrib import admin
from .models import Opony
# Register your models here.
@admin.register(Opony)
class OponyAdmin(admin.ModelAdmin):
    list_display = ["producent", "zdjecie"]
