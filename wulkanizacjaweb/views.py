from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Opony
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


def usun_opone(request, id):
    opona = get_object_or_404(Opony, pk=id)

    if request.method =="POST":
        opona.delete()
        return redirect(wszystkie_opony)

    return render(request, 'potwierdz.html', {'opona': opona})