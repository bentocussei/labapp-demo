from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import EmailValidator


class Escola(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome da Escola", unique=True)
    email = models.EmailField(max_length=255, verbose_name="E-mail da Escola", validators=[EmailValidator()])
    numero_salas = models.PositiveIntegerField(verbose_name="Número de Salas")
    provincia = ArrayField(models.CharField(max_length=255), verbose_name="Província")

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']  # Por padrão, ordenar por nome
