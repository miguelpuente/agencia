from django import forms

from django.contrib.auth.models import User, Group
from .models import Perfil


class RegistroForm(forms.Form):
    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput()
    )
    username = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.TextInput()
    )
    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )
    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )

    def clean(self):
        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Las contraseñas no coinciden.')

        return data

    def save(self):
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        perfil = Perfil(user=user)
        perfil.save()

        Group.objects.get_or_create(name='Administrador')
        Group.objects.get_or_create(name='Colaborador')
        grupo, creado = Group.objects.get_or_create(name='Registrado')

        user.groups.add(grupo)

        return user
