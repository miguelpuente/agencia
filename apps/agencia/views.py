from django.views.generic import ListView
from .models import Auto

class AutoListView(ListView):
    model = Auto
    template_name = 'agencia/auto/lista_autos.html'
    context_object_name = 'autos'