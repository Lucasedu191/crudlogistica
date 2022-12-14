from datetime import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import DateField





class Caracterisca(models.Model):
    TIPO_CHOICES = (
        ("Nav", "Navio"),
        ("Avi", "Avião"),
        ("Cam", "Caminhão"),
        ("Oni", "Onibus"),
        ("Van", "Van"),
        ("Car", "Carro"),
        ("Mot", "Moto"),
        ("Bic", "Bicicleta"),
    )

    matricula = models.CharField('Matricula', max_length=100)
    tipo = models.CharField(max_length=3, choices=TIPO_CHOICES, blank=False, null=False)
    ano: DateField = models.DateField(null=False, blank=False)
    quantidade = models.IntegerField('Quantidade de veículos')
    modelo = models.CharField('Modelo', max_length=100)

    def __str__(self):
        return self.matricula


class Veiculo(models.Model):
    caracteristica = models.ForeignKey(Caracterisca, on_delete=models.CASCADE, null=True)
    nome = models.CharField('Nome', max_length=100)
    tipo = models.CharField('Tipo', max_length=100)
    quantidade = models.IntegerField('Quantidade de veículos')

    def __str__(self):
        return self.nome


class TipoContrato(models.Model):
    TIPO_CONTRATO_CHOICES = (
        ("cole", "Coleta"),
        ("entr", "Entrega"),
        ("desp", "Despachar"),
    )

    FATURADO_CHOICES = (
        ("pago", "Pago"),
        ("npag", "Não Pagou"),
        ("rece", "A receber"),
    )

    nome = models.CharField('Matricula', max_length=100)
    tipo_contrato = models.CharField(max_length=4, choices=TIPO_CONTRATO_CHOICES, blank=False, null=False)
    faturado = models.CharField(max_length=4, choices=FATURADO_CHOICES, blank=False, null=False)
    ano = models.DateField(null=False, blank=False)

    def __str__(self):
        return self.nome

class Cliente(models.Model):

    contrato = models.ForeignKey(TipoContrato, on_delete=models.CASCADE, null=True)
    nome = models.CharField('Nome', max_length=100)
    cnpj = models.CharField('CNPJ', max_length=100)
    celular = models.CharField('Celular', max_length=100)

    def __str__(self):
        return self.nome


class Agendar(models.Model):

    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, null=True)
    contrato = models.ForeignKey(TipoContrato, on_delete=models.DO_NOTHING, null=True)
    data = models.DateField(null=False, blank=False)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.DO_NOTHING, null=True)
    celular = models.CharField('Celular', max_length=100)
    orcamento = models.CharField('Orçamento', max_length=100, null=True)

    def __str__(self):
        return self.cliente.nome