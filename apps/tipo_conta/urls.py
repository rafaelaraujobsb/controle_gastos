from django.urls import path

from .views import ListarTipoConta, CadastrarTipoConta, RemoverTipoConta, AtualizarTipoConta


urlpatterns = [
    path('', ListarTipoConta.as_view(), name="listar_tipo_conta"),
    path('cadastrar', CadastrarTipoConta.as_view(), name="cadastrar_tipo_conta"),
    path('deletar/<int:pk>', RemoverTipoConta.as_view(), name='deletar_tipo_conta'),
    path('atualizar/<int:pk>', AtualizarTipoConta.as_view(), name='atualizar_tipo_conta'),
]
