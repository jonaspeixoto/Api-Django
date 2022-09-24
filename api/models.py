from django.db import models

# Create your models here.


class Tecnologia(models.Model):
    nome = models.CharField(max_length=20, null= False, blank=False)

    def __str__(self):
        return self.nome


class Vaga(models.Model):
    CONTRATACAO_CHOISE = [
        ('CLT', 'Empregado registado pela CLT'),
        ('PJ', 'Pessoa Juridica'),
    ]
    titulo = models.CharField(max_length=50, null=False, blank=False)
    decricao = models.TextField(null=False, blank=False)
    salario = models.FloatField(null=True, blank=False)
    local = models.CharField(max_length=20, null= False, blank=False)
    quantidade = models.IntegerField(null=False, blank=False)
    contato = models.EmailField(null=False, blank = False)
    tipo_contratacao = models.CharField(max_length=3 , null=False, blank=False, choices=CONTRATACAO_CHOISE)
    teclonogias = models.ManyToManyField(Tecnologia)

    def __str__(self):
        return self.titulo


