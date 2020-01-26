from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from .models import TipoConta


class ListarTipoConta(ListView):
    model = TipoConta


class CadastrarTipoConta(CreateView):
    model = TipoConta
    fields = ["descricao"]


class AtualizarTipoConta(UpdateView):
    model = TipoConta
    fields = ["descricao"]
    # template_name = 'update.html'


class RemoverTipoConta(DeleteView):
    model = TipoConta
    success_url = reverse_lazy('listar_tipo_conta')
