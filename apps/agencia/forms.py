from django import forms
from .models import Comentario


class CrearComentarioForm(forms.ModelForm):

    comentario = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Comentario
        fields = ('user', 'perfil', 'auto', 'comentario')
