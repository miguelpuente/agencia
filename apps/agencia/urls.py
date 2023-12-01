from django.urls import path
from .views import (
    ModeloListView, ModeloDetailView, ModeloCreateView, ModeloUpdateView, ModeloDeleteView
    )

urlpatterns = [
    # Rutas para el modelo Modelo
    path('modelo/list/', ModeloListView.as_view(), name='modelo_list'),
    path('modelo/<int:pk>/', ModeloDetailView.as_view(), name='modelo_detail'),
    path('modelo/create/', ModeloCreateView.as_view(), name='modelo_create'),
    path('modelo/<int:pk>/update/', ModeloUpdateView.as_view(), name='modelo_update'),
    path('modelo/<int:pk>/delete/', ModeloDeleteView.as_view(), name='modelo_delete'),
]
