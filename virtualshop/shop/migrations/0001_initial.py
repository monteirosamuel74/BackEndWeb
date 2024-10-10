# Generated by Django 5.1.2 on 2024-10-10 00:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
                'ordering': ['nome'],
                'indexes': [models.Index(fields=['nome'], name='shop_catego_nome_43d445_idx')],
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('imagem', models.ImageField(blank=True, upload_to='produtos/%Y/%m/%d')),
                ('descricao', models.TextField(blank=True)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('disponivel', models.BooleanField(default=True)),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('atualizado', models.DateTimeField(auto_now=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produtos', to='shop.categoria')),
            ],
        ),
    ]