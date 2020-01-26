from django.urls import path

from .views import ListarCartao, CadastrarCartao


urlpatterns = [
    path('', ListarCartao.as_view(), name="listar_cartao"),
    path('cadastrar', CadastrarCartao.as_view(), name="cadastrar_cartao"),
    path('deletar/<int:pk>', ListarCartao.as_view(), name='deletar_cartao'),
    path('atualizar/<int:pk>', ListarCartao.as_view(), name='atualizar_cartao'),
]
