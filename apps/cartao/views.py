from django.shortcuts import render
from django.views.generic import ListView, CreateView

from .models import Cartao


class ListarCartao(ListView):
    model = Cartao


class CadastrarCartao(CreateView):
    model = Cartao
    fields = ["descricao", "limite", "dia_fechamento", "dia_pagamento", "conta_id"]
