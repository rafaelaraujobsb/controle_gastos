from django.urls import path

from .views import ListarUsuario, CadastrarUsuario, RemoverUsuario, AtualizarUsuario


urlpatterns = [
    path('', ListarUsuario.as_view(), name="listar_usuario"),
    path('cadastrar', CadastrarUsuario.as_view(), name="cadastrar_usuario"),
    path('deletar/<int:pk>', RemoverUsuario.as_view(), name='deletar_usuario'),
    path('atualizar/<int:pk>', AtualizarUsuario.as_view(), name='atualizar_usuario'),
]
