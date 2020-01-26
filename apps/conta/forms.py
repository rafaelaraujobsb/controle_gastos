from django.db import models
from django.forms import ModelForm

from .models import Conta


class ContaForm(ModelForm):
    class Meta:
        model = Conta
        exclude = ["data_cadastro"]
