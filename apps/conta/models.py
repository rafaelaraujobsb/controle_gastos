from django.db import models

from apps.tipo_conta.models import TipoConta


class Conta(models.Model):
    descricao = models.CharField(max_length=50)
    valor_inicial = models.DecimalField(max_digits=10, decimal_places=2)
    data_cadastro = models.PositiveIntegerField()
    somatorio = models.BooleanField()
    tipo_conta_id = models.ForeignKey(TipoConta, on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao
