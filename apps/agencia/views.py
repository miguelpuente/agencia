from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Marca, Auto, Comentario
from .forms import CrearComentarioForm, AutoForm


class AutoCreateView(CreateView):
    model = Auto
    form_class = AutoForm
    template_name = 'agencia/auto/crear_auto.html'
    success_url = reverse_lazy('agencia:inicio')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.perfil = self.request.user.perfil
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accion'] = 'Agregar Auto'
        return context

class AutoUpdateView(UpdateView):
    model = Auto
    form_class = AutoForm
    template_name = 'agencia/auto/crear_auto.html'
    slug_field = 'url'
    slug_url_kwarg = 'url'
    success_url = reverse_lazy('agencia:inicio')


    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.perfil = self.request.user.perfil
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accion'] = 'Actualizar Auto'
        return context
    
class AutoDeleteView(DeleteView):
    model = Auto
    slug_field = 'url'
    slug_url_kwarg = 'url'
    success_url = reverse_lazy('agencia:inicio')
    
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
        context['comentarios'] = Comentario.objects.filter(
            visible=True, auto=self.get_object()).all()
        context['cantidad_comentarios'] = Comentario.objects.filter(
            visible=True, auto=self.get_object()).all().count()
        return context


class ComentarioView(UserPassesTestMixin, View):
    template_name = 'agencia/detalle.html'

    def test_func(self):
        allowed_groups = ['Colaborador', 'Administrador', 'Registrado']
        return self.request.user.is_authenticated and any(self.request.user.groups.filter(name=group).exists() for group in allowed_groups)

    def get(self, request, *args, **kwargs):
        return HttpResponse(status=405)

    def post(self, request, *args, **kwargs):
        url = request.POST.get('url')
        auto = {
            'user': request.user.id,
            'perfil': request.user.perfil.id,
            'comentario': request.POST.get('comentario'),
            'auto': request.POST.get('auto')
        }
        form = CrearComentarioForm(auto)
        if form.is_valid():
            form.save()
            return redirect('agencia:detalle', url=url)
        else:
            return HttpResponse(status=500)


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
