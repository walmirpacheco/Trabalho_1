# Generated by Django 2.2.4 on 2022-12-26 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cad_Ciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('data_nasc', models.DateField(verbose_name='Data de Nascimento')),
                ('sexo', models.CharField(choices=[['F', 'Feminino'], ['M', 'Masculino'], ['N', 'Nenhuma das opções']], max_length=1)),
                ('endereco', models.CharField(max_length=100, verbose_name='Endereço')),
                ('email', models.CharField(max_length=50, verbose_name='E-mail')),
            ],
        ),
    ]
