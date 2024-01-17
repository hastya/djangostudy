# Generated by Django 5.0 on 2024-01-17 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_sphere'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='email',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True, verbose_name='email'),
        ),
        migrations.AddField(
            model_name='sphere',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активно'),
        ),
    ]