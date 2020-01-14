from django.db import models

from apps.cartao.models import Cartao


class Parcelamento(models.Model):
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField()
    data_final = models.PositiveIntegerField()
    cartao_id = models.ForeignKey(Cartao, on_delete=models.PROTECT)

    def __str__(self):
        return self.valor_total
