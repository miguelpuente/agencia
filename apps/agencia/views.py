from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
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


class NosotrosTemplateView(TemplateView):
    template_name = 'agencia/nosotros.html'


class ContactoTemplateView(TemplateView):
    template_name = 'agencia/contacto.html'


class AutoDetailView(DetailView):
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


class MarcaListView(ListView):
    model = Auto
    template_name = 'agencia/index.html'
    context_object_name = 'autos'
    paginate_by = 2
    ordering = ('-creado',)

    def get_queryset(self):
        auto = None
        if self.kwargs['marca_id']:
            marca_id = self.kwargs['marca_id']
            marca = Marca.objects.filter(id=marca_id)[:1]
            auto = Auto.objects.filter(visible=True, marca_modelo__marca=marca)
        return auto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marcas'] = Marca.objects.all()
        context['autos_destacados'] = Auto.objects.filter(
            destacado=True, visible=True)
        return context


class UserListView(ListView):
    model = Auto
    template_name = 'agencia/index.html'
    context_object_name = 'autos'
    paginate_by = 2
    ordering = ('-creado',)

    def get_queryset(self):
        auto = None
        if self.kwargs['nombre']:
            user_nombre = self.kwargs['nombre']
            user = User.objects.filter(username=user_nombre)[:1]
            auto = Auto.objects.filter(visible=True, user=user)
        return auto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marcas'] = Marca.objects.all()
        context['autos_destacados'] = Auto.objects.filter(
            destacado=True, visible=True)
        return context
