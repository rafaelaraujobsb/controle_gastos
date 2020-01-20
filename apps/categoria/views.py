from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from .models import Categoria


class ListarCategoriaGasto(ListView):
    model = Categoria


class CadastrarCategoriaGasto(CreateView):
    model = Categoria
    fields = ["descricao"]


class AtualizarCategoriaGasto(UpdateView):
    model = Categoria
    fields = ["descricao"]
    # template_name = 'update.html'


class RemoverCategoriaGasto(DeleteView):
    model = Categoria
    success_url = reverse_lazy('listar_categoria')
