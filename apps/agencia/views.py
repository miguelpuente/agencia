from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Modelo


class ModeloListView(ListView):
    model = Modelo
    template_name = 'agencia/modelos/modelo_list.html'
    context_object_name = 'modelos'

class ModeloDetailView(DetailView):
    model = Modelo
    template_name = 'agencia/modelos/modelo_detail.html'
    context_object_name = 'modelo'

class ModeloCreateView(CreateView):
    model = Modelo
    template_name = 'agencia/modelos/modelo_form.html'
    context_object_name = 'modelo'
    fields = '__all__'
    success_url = reverse_lazy('modelo_list')

class ModeloUpdateView(UpdateView):
    model = Modelo
    template_name = 'agencia/modelos/modelo_form.html'
    context_object_name = 'modelo'
    fields = '__all__'
    success_url = reverse_lazy('modelo_list')

class ModeloDeleteView(DeleteView):
    model = Modelo
    template_name = 'agencia/modelos/modelo_confirm_delete.html'
    context_object_name = 'modelo'
    success_url = reverse_lazy('modelo_list')







