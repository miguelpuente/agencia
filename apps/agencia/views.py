import os
from typing import Any
from django.db import models
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Modelo, Marca, MarcaModelo, Auto


class InicioListView(ListView):
    model = Auto
    template_name = 'agencia/index.html'
    context_object_name = 'autos'
    paginate_by = 2
    ordering = ('-creado',)
    queryset = Auto.objects.filter(visible=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marcas'] = Marca.objects.all()
        context['autos_destacados'] = Auto.objects.filter(
            destacado=True, visible=True)
        return context


class AutoDetailView(DeleteView):
    model = Auto
    template_name = 'agencia/detalle.html'
    context_object_name = 'auto'
    slug_field = 'url'
    slug_url_kwarg = 'url'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['autos'] = Auto.objects.filter(visible=True)
        context['marcas'] = Marca.objects.all()
        return context
