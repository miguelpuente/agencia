from django.urls import path
from .views import InicioListView, NosotrosTemplateView, ContactoTemplateView, AutoDetailView, ComentarioView, MarcaListView, UserListView

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
        view=ContactoTemplateView.as_view(),
        name='contacto'
    ),
    path(
        route='auto/<slug:url>/',
        view=AutoDetailView.as_view(),
        name='detalle'
    ),
    path(
        route='comentario/',
        view=ComentarioView.as_view(),
        name='comentario'
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
