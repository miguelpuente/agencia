from django.urls import path
from .views import (
    ModeloListView, ModeloDetailView, ModeloCreateView, ModeloUpdateView, ModeloDeleteView,
    MarcaListView, MarcaDetailView, MarcaCreateView, MarcaUpdateView, MarcaDeleteView,
    MarcaModeloListView, MarcaModeloDetailView, MarcaModeloCreateView, MarcaModeloUpdateView, MarcaModeloDeleteView,
    )

urlpatterns = [
    # Rutas para el modelo Modelo
    path('modelo/list/', ModeloListView.as_view(), name='modelo_list'),
    path('modelo/<int:pk>/', ModeloDetailView.as_view(), name='modelo_detail'),
    path('modelo/create/', ModeloCreateView.as_view(), name='modelo_create'),
    path('modelo/<int:pk>/update/', ModeloUpdateView.as_view(), name='modelo_update'),
    path('modelo/<int:pk>/delete/', ModeloDeleteView.as_view(), name='modelo_delete'),

    # Rutas para el modelo Marca
    path('marca/list/', MarcaListView.as_view(), name='marca_list'),
    path('marca/<int:pk>/', MarcaDetailView.as_view(), name='marca_detail'),
    path('marca/create/', MarcaCreateView.as_view(), name='marca_create'),
    path('marca/<int:pk>/update/', MarcaUpdateView.as_view(), name='marca_update'),
    path('marca/<int:pk>/delete/', MarcaDeleteView.as_view(), name='marca_delete'),

    # Rutas para el modelo MarcaModelo
    path('marca-modelo/list/', MarcaModeloListView.as_view(),
         name='marca_modelo_list'),
    path('marca-modelo/<int:pk>/', MarcaModeloDetailView.as_view(),
         name='marca_modelo_detail'),
    path('marca-modelo/create/', MarcaModeloCreateView.as_view(),
         name='marca_modelo_create'),
    path('marca-modelo/<int:pk>/update/',
         MarcaModeloUpdateView.as_view(), name='marca_modelo_update'),
    path('marca-modelo/<int:pk>/delete/',
         MarcaModeloDeleteView.as_view(), name='marca_modelo_delete'),
]
