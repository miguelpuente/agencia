from django.contrib import admin
from .models import Auto, Marca, Modelo, MarcaModelo, Comentario


@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'titulo', 'marca_modelo',
                    'destacado', 'visible', 'imagen')
    search_fields = ('titulo', 'user__username', 'user__email')
    list_filter = ('creado', 'modificado')
    list_editable = ('marca_modelo', 'destacado', 'visible',)

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ('url',)
        form = super(AutoAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['user'].initial = request.user
        form.base_fields['perfil'].initial = request.user.perfil
        return form


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


@admin.register(MarcaModelo)
class MarcaModeloAdmin(admin.ModelAdmin):
    list_display = ('id', 'marca', 'modelo')


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'auto', 'comentario', 'visible')
