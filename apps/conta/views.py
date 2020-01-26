from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Conta
from .forms import ContaForm


class ListarConta(ListView):
    model = Conta


class CadastrarConta(CreateView):
    model = Conta
    form_class = ContaForm
    template_name = 'conta/conta_form.html'
    success_url = reverse_lazy('listar_conta')


class AtualizarConta(UpdateView):
    model = Conta
    form_class = ContaForm
    template_name = 'conta/conta_form.html'
    success_url = reverse_lazy('listar_conta')


class RemoverConta(DeleteView):
    model = Conta
    success_url = reverse_lazy('listar_conta')
