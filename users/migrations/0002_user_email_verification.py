# Generated by Django 4.2 on 2024-01-20 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_verification',
            field=models.CharField(blank=True, max_length=35, null=True, verbose_name='код верификации email'),
        ),
    ]
