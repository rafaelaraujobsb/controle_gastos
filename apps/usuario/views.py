from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from .models import Usuario


class ListarUsuario(ListView):
    model = Usuario


class CadastrarUsuario(CreateView):
    model = Usuario
    fields = ["matricula", "nome"]


class AtualizarUsuario(UpdateView):
    model = Usuario
    fields = ["nome"]
    # template_name = 'update.html'


class RemoverUsuario(DeleteView):
    model = Usuario
    success_url = reverse_lazy('listar_usuario')
