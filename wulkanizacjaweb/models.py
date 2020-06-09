from django.db import models

# Create your models here.


class Opony(models.Model):
    producent = models.CharField(max_length=32, blank=False)
    szerokosc = models.PositiveSmallIntegerField(default=0)
    profil = models.PositiveSmallIntegerField(default=0)
    srednica = models.PositiveSmallIntegerField(default=0)
    opis = models.TextField(blank=True, default="")
    rok_produkcji = models.DateField(default=2000)
    zdjecie = models.ImageField(upload_to="plakaty", null=True, blank=True)

    def __str__(self):
        return self.producent_rok_produkcji()

    def producent_rok_produkcji(self):
        return "{} ({})" .format(self.producent, self.rok_produkcji)

class Koszyk(models.Model):
    lista_zakupow = Opony


    def __str__(self):
        return self.lista_zakupow()

