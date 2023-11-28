from django.urls import path
from .views import AutoListView

urlpatterns = [
    path('lista-autos', AutoListView.as_view(), name='lista-autos')
]
