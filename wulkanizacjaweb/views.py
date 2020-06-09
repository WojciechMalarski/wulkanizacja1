from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Opony, Koszyk
from .forms import OponaForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def wszystkie_opony(request):
    wszystkie = Opony.objects.all()
    return render(request, 'opony.html', {'opony': wszystkie})

@login_required
def nowa_opona(request):
     form = OponaForm(request.POST or None, request.FILES or None)

     if form.is_valid():
         form.save()
         return redirect(wszystkie_opony)

     return render(request, 'opona_form.html', {'form': form})

@login_required
def edytuj_opone(request, id):
     opona = get_object_or_404(Opony,  pk=id)
     form = OponaForm(request.POST or None, request.FILES or None, instance=opona)

     if form.is_valid():
          form.save()
          return redirect(wszystkie_opony)

     return render(request, 'opona_form.html', {'form': form})

@login_required
def usun_opone(request, id):
    opona = get_object_or_404(Opony, pk=id)

    if request.method =="POST":
        opona.delete()
        return redirect(wszystkie_opony)

    return render(request, 'potwierdz.html', {'opona': opona})

@login_required
def kup_opone(request, id):
    opona = get_object_or_404(Opony, pk=id)
    kupiona_opona = OponaForm(request.POST or None, request.FILES or None, instance=opona)
    if request.method =="POST":
        kupiona_opona.save()
        return redirect(wszystkie_opony)
    return render(request, 'koszyk.html', {'koszyk': kupiona_opona})


def rejestracja(request, id):
    return render(request, 'rejestracja.html', {'opony'})



