from django.db import models
from datetime import datetime

class Receita(models.Model):
    nome_das_receitas = models.CharField(max_length=100)
    modo_de_preparo = models.TextField(max_length=300)
    ingredientes = models.TextField()
    tempo_de_preparo = models.CharField(max_length=100)
    redimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    criado_em = models.DateTimeField(default=datetime.now, blank=True)