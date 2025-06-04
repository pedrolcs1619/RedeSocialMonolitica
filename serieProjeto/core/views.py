from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Filme

class FilmeListView(ListView):
    model = Filme
    template_name = 'catalogo/lista.html'  # Template localizado em core/templates/catalogo/lista.html
    context_object_name = 'filmes'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        ano = self.request.GET.get('ano')
        ordem = self.request.GET.get('ordem', 'titulo')
        if ano:
            queryset = queryset.filter(ano_lancamento=ano)
        return queryset.order_by(ordem)

class FilmeDetailView(DetailView):
    model = Filme
    template_name = 'catalogo/detalhe.html'  # Template para o detalhe

class FilmeCreateView(CreateView):
    model = Filme
    fields = ['titulo', 'descricao', 'ano_lancamento', 'imagem']
    template_name = 'catalogo/form.html'  # Template de formulário para criar
    success_url = reverse_lazy('lista_filmes')

class FilmeUpdateView(UpdateView):
    model = Filme
    fields = ['titulo', 'descricao', 'ano_lancamento', 'imagem']
    template_name = 'catalogo/form.html'  # Pode reaproveitar o mesmo form.html
    success_url = reverse_lazy('lista_filmes')

class FilmeDeleteView(DeleteView):
    model = Filme
    template_name = 'catalogo/confirmar_delete.html'  # Template de confirmação
    success_url = reverse_lazy('lista_filmes')
