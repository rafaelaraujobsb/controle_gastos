from django.urls import path

from .views import ListarCategoriaGasto, CadastrarCategoriaGasto, RemoverCategoriaGasto, AtualizarCategoriaGasto


urlpatterns = [
    path('', ListarCategoriaGasto.as_view(), name="listar_categoria"),
    path('cadastrar', CadastrarCategoriaGasto.as_view(), name="cadastrar_categoria"),
    path('deletar/<int:pk>', RemoverCategoriaGasto.as_view(), name='deletar_categoria'),
    path('atualizar/<int:pk>', AtualizarCategoriaGasto.as_view(), name='atualizar_categoria'),
]
