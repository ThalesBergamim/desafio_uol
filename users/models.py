from django.db import models
from django.core.validators import RegexValidator


class Group(models.TextChoices):
    VINGADORES = 'V', 'Vingadores'
    LIGA_DA_JUSTICA = 'L', 'Liga da Justiça'

class Users(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    email = models.EmailField(verbose_name='E-mail')
    telephone = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        verbose_name='Telefone',
        validators=[RegexValidator(
            regex=r'^\(?\d{2}\)?\s?\d{4,5}-?\d{4}',
            message='Número de telefone inválido. Utilize o formato (XX) XXXX-XXXX',
        )],
        help_text='Utilize o formato (XX) XXXX-XXXX'
    )
    codename = models.CharField(max_length=255)
    group = models.CharField(
        max_length=255, 
        choices=Group.choices,
        default=Group.LIGA_DA_JUSTICA,
        verbose_name='Grupo',
        help_text='Escolha um grupo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name