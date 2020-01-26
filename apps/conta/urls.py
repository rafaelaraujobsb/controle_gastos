from django.urls import path

from .views import ListarConta, CadastrarConta, AtualizarConta, RemoverConta


urlpatterns = [
    path('', ListarConta.as_view(), name="listar_conta"),
    path('cadastrar', CadastrarConta.as_view(), name="cadastrar_conta"),
    path('deletar/<int:pk>', RemoverConta.as_view(), name='deletar_conta'),
    path('atualizar/<int:pk>', AtualizarConta.as_view(), name='atualizar_conta'),
]
