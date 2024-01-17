# Generated by Django 5.0 on 2024-01-17 08:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sphere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название сферы применения')),
                ('description', models.TextField(verbose_name='Описание сферы применения')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='продукт')),
            ],
            options={
                'verbose_name': 'сфера',
                'verbose_name_plural': 'сферы',
            },
        ),
    ]
