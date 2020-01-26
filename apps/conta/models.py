from time import time

from django.db import models
from django.urls import reverse

from apps.tipo_conta.models import TipoConta


class Conta(models.Model):
    descricao = models.CharField(max_length=50, verbose_name="Descrição")
    valor_inicial = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor em Conta")
    data_cadastro = models.PositiveIntegerField(verbose_name="Data Cadastro")
    somatorio = models.BooleanField(verbose_name="Incluir no Somatorio")
    tipo_conta_id = models.ForeignKey(TipoConta, on_delete=models.PROTECT, verbose_name="Tipo da Conta")

    def save(self, *args, **kwargs):
        self.data_cadastro = int(time())
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('listar_conta')

    def __str__(self):
        return self.descricao
