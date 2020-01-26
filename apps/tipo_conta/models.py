from django.db import models
from django.urls import reverse


class TipoConta(models.Model):
    descricao = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('listar_tipo_conta')

    def __str__(self):
        return self.descricao
