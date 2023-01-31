# Generated by Django 4.1.4 on 2022-12-12 23:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('thumb', models.ImageField(upload_to='thumb_filmes')),
                ('categoria', models.CharField(choices=[('ANALISES', 'analises'), ('PROGRAMACAO', 'Programação'), ('APRESENTACAO', 'Apresentação'), ('OUTROS', 'Outros')], max_length=20)),
                ('visualizacoes', models.IntegerField(default=0)),
                ('descricao', models.CharField(max_length=1000)),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]