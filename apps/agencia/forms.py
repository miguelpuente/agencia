from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Comentario, Auto, MarcaModelo


class CrearComentarioForm(forms.ModelForm):

    comentario = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Comentario
        fields = ('user', 'perfil', 'auto', 'comentario')


class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ['titulo', 'resumen', 'contenido', 'destacado', 'marca_modelo',
                  'visible', 'anio', 'km', 'color', 'precio', 'transmision', 'estado', 'imagen']

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
        widget=forms.CheckboxInput(),
    )
    marca_modelo = forms.ModelChoiceField(
        queryset=MarcaModelo.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    visible = forms.BooleanField(
        widget=forms.CheckboxInput()
    )
