from django.db import models
from django.urls import reverse


class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    matricula = models.IntegerField(primary_key=True)

    def get_absolute_url(self):
        return reverse('listar_usuario')

    def __str__(self):
        return self.nome
