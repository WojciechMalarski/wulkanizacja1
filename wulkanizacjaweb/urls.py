from wulkanizacjaweb.views import wszystkie_opony
from django.urls import path
from wulkanizacjaweb.views import wszystkie_opony, nowa_opona, edytuj_opone, usun_opone, kup_opone, rejestracja

urlpatterns = [
    path('wszystkie/', wszystkie_opony, name="wszystkie_opony"),
    path('nowa/', nowa_opona, name="nowa_opona"),
    path('edytuj/<int:id>', edytuj_opone, name="edytuj_opone"),
    path('usun/<int:id>', usun_opone, name="usun_opone"),
    path('kup/<int:id>', kup_opone, name="kup_opone"),
    path('rejestracja/', rejestracja, name="rejestracja"),


    #path('', views.index, name='index'),
    #path('index/', index, name="index"),
]
