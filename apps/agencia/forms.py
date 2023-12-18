from django import forms
from django.db import models
from ckeditor.widgets import CKEditorWidget
from .models import Comentario, Auto, MarcaModelo


class CrearComentarioForm(forms.ModelForm):

    comentario = forms.CharField(
        required=True,
        widget=forms.Textarea())

    class Meta:
        model = Comentario
        fields = ('user', 'perfil', 'auto', 'comentario')


class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ['titulo', 'resumen', 'contenido', 'destacado', 'marca_modelo',
                  'visible', 'precio', 'anio', 'km', 'color', 'transmision', 'estado', 'imagen']

    titulo = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'})
    )
    resumen = forms.CharField(
        widget=CKEditorWidget(
            attrs={'class': 'form-control'})
    )
    contenido = forms.CharField(
        widget=CKEditorWidget(
            attrs={'class': 'form-control'})
    )
    destacado = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(),
    )
    marca_modelo = forms.ModelChoiceField(
        queryset=MarcaModelo.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    visible = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
    )
    anio = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    km = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    color = forms.CharField(
        widget=forms.Select(
            choices=Auto.Color.choices,
            attrs={'class': 'form-control'})
    )
    precio = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    transmision = forms.CharField(
        widget=forms.Select(
            choices=Auto.Transmision.choices,
            attrs={'class': 'form-control'})
    )
    estado = forms.CharField(
        widget=forms.Select(
            choices=Auto.Estado.choices,
            attrs={'class': 'form-control'})
    )
    imagen = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'form-control-file'})
    )