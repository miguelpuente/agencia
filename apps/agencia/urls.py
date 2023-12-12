from django.urls import path
from .views import InicioListView, AutoDetailView

app_name = 'apps.agencia'

urlpatterns = [
    path(
        route='',
        view=InicioListView.as_view(),
        name='inicio'
    ),
    path(
        route='auto/<slug:url>/',
        view=AutoDetailView.as_view(),
        name='detalle'
    ),

]
