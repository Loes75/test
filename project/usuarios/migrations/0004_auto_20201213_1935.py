# Generated by Django 3.1.4 on 2020-12-14 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20201213_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='latitud',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='longitud',
            field=models.IntegerField(blank=True),
        ),
    ]
