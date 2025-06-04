from django.urls import path
from .views import *

urlpatterns = [
    path('', FilmeListView.as_view(), name='lista_filmes'),
    path('filme/<int:pk>/', FilmeDetailView.as_view(), name='detalhe_filme'),
    path('filme/novo/', FilmeCreateView.as_view(), name='criar_filme'),
    path('filme/<int:pk>/editar/', FilmeUpdateView.as_view(), name='editar_filme'),
    path('filme/<int:pk>/excluir/', FilmeDeleteView.as_view(), name='excluir_filme'),
]
