from django.db import models

from apps.conta.models import Conta


class Cartao(models.Model):
    descricao = models.CharField(max_length=50, verbose_name="Descrição")
    limite = models.DecimalField(max_digits=10, decimal_places=2)
    dia_fechamento = models.PositiveIntegerField(verbose_name="Dia do Fechamento")
    dia_pagamento = models.PositiveIntegerField(verbose_name="Dia do Pagamento")
    conta_id = models.ForeignKey(Conta, on_delete=models.PROTECT, verbose_name="Conta")


    def __str__(self):
        return self.descricao
