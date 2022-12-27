from django.db import models

sexo_choices = [
    ['F', 'Feminino'],
    ['M', 'Masculino'],
    ['N', 'Nenhuma das opções'],
]

class Cad_Funcionario(models.Model):
    nome = models.CharField('Nome', max_length=100)
    data_nasc = models.DateField('Data de Nascimento')
    sexo = models.CharField(max_length=1, choices=sexo_choices)
    endereco = models.CharField('Endereço', max_length=100)
    email = models.CharField('E-mail', max_length=50)

    def __str__(self):
        return self.nome

class Cad_Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    data_nasc = models.DateField('Data de Nascimento')
    sexo = models.CharField(max_length=1, choices=sexo_choices)
    endereco = models.CharField('Endereço', max_length=100)
    email = models.CharField('E-mail', max_length=50)

    def __str__(self):
        return self.nome


