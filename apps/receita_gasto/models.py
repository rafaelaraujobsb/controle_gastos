from django.db import models

from apps.conta.models import Conta
from apps.categoria.models import Categoria
from apps.parcelamento.models import Parcelamento


class ReceitaGasto(models.Model):
    descricao = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.PositiveIntegerField()
    categoria_id = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    conta_id = models.ForeignKey(Conta, on_delete=models.PROTECT, null=True, blank=True)
    parcelamento_id = models.ForeignKey(Parcelamento, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.descricao
