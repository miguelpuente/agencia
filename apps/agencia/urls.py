from django.urls import path
from .views import InicioListView, NosotrosTemplateView, ContactoFormView, ContactoTemplateView, AutoDetailView, AutoCreateView, AutoUpdateView, AutoDeleteView, ComentarioCreateView, ComentarioDeleteView, MarcaListView, UserListView

app_name = 'apps.agencia'

urlpatterns = [
    path(
        route='',
        view=InicioListView.as_view(),
        name='inicio'
    ),
    path(
        route='nosotros/',
        view=NosotrosTemplateView.as_view(),
        name='nosotros'
    ),
    path(
        route='contacto/',
        view=ContactoFormView.as_view(),
        name='contacto'
    ),
    path(
        route='contactook/',
        view=ContactoTemplateView.as_view(),
        name='contactook'
    ),
    path(
        route='auto/<slug:url>/',
        view=AutoDetailView.as_view(),
        name='detalle'
    ),
    path(
        route='carga_auto/',
        view=AutoCreateView.as_view(),
        name='carga_auto'
    ),
    path(
        route='actualizar_auto/<slug:url>/',
        view=AutoUpdateView.as_view(),
        name='actualizar_auto'
    ),
    path(
        route='eliminar_auto/<slug:url>/',
        view=AutoDeleteView.as_view(),
        name='eliminar_auto'
    ),
    path(
        route='comentario/',
        view=ComentarioCreateView.as_view(),
        name='comentario'
    ),
    path(
        route='eliminar_comentario/<int:pk>/',
        view=ComentarioDeleteView.as_view(),
        name='eliminar_comentario'
    ),
    path(
        route='marca/<int:marca_id>/',
        view=MarcaListView.as_view(),
        name='marca'
    ),
    path(
        route='user/<str:nombre>/',
        view=UserListView.as_view(),
        name='user'
    ),
]
