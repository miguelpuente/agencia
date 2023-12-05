from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Modelo, Marca, MarcaModelo, Auto

# CRUD Modelo
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


# CRUD Marca

class MarcaListView(ListView):
    model = Marca
    template_name = 'agencia/marcas/marca_list.html'
    context_object_name = 'marcas'


class MarcaDetailView(DetailView):
    model = Marca
    template_name = 'agencia/marcas/marca_detail.html'
    context_object_name = 'marca'


class MarcaCreateView(CreateView):
    model = Marca
    template_name = 'agencia/marcas/marca_form.html'
    context_object_name = 'marca'
    fields = '__all__'
    success_url = reverse_lazy('marca_list')


class MarcaUpdateView(UpdateView):
    model = Marca
    template_name = 'agencia/marcas/marca_form.html'
    context_object_name = 'marca'
    fields = '__all__'
    success_url = reverse_lazy('marca_list')


class MarcaDeleteView(DeleteView):
    model = Marca
    template_name = 'agencia/marcas/marca_confirm_delete.html'
    context_object_name = 'marca'
    success_url = reverse_lazy('marca_list')


# CRUD MarcaModelo

class MarcaModeloListView(ListView):
    model = MarcaModelo
    template_name = 'agencia/marcasmodelos/marca_modelo_list.html'
    context_object_name = 'marcasmodelos'


class MarcaModeloDetailView(DetailView):
    model = MarcaModelo
    template_name = 'agencia/marcasmodelos/marca_modelo_detail.html'
    context_object_name = 'marcamodelo'


class MarcaModeloCreateView(CreateView):
    model = MarcaModelo
    template_name = 'agencia/marcasmodelos/marca_modelo_form.html'
    context_object_name = 'marcamodelo'
    fields = '__all__'
    success_url = reverse_lazy('marca_modelo_list')


class MarcaModeloUpdateView(UpdateView):
    model = MarcaModelo
    template_name = 'agencia/marcasmodelos/marca_modelo_form.html'
    fields = '__all__'
    success_url = reverse_lazy('marca_modelo_list')


class MarcaModeloDeleteView(DeleteView):
    model = MarcaModelo
    template_name = 'agencia/marcasmodelos/marca_modelo_confirm_delete.html'
    success_url = reverse_lazy('marca_modelo_list')

