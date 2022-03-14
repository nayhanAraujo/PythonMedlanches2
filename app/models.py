from django.db import models

# Create your models here.

class Carros(models.Model):
    modelo = models.CharField(max_length=150)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField()

class Lanches(models.Model):
    nome = models.CharField(max_length=150)
    tipo = models.CharField(max_length=150)
    data_pedido = models.CharField(max_length=150)
    horario = models.CharField(max_length=150)
    qtd = models.IntegerField()
    total = models.DecimalField(max_digits=5, decimal_places=2)
    status_pgto = models.CharField(max_length=150)
    tipo_pgto = models.CharField(max_length=150)
    data_pgto = models.CharField(max_length=150)


