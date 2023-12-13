from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import TemplateView, FormView
from .forms import RegistroForm


class RegistroView(FormView):
    form_class = RegistroForm
    template_name = 'user/registro.html'
    success_url = reverse_lazy('auth:registrook')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response


class RegistroOkTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'user/registrook.html'


class LoginView(LoginView):
    template_name = 'user/login.html'


class SalirView(LoginRequiredMixin, LogoutView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse_lazy('auth:login'))
