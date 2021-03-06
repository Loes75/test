# Generated by Django 3.1.4 on 2020-12-13 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=40)),
                ('ciudad', models.CharField(max_length=40)),
                ('direccion', models.CharField(max_length=100)),
                ('geoestado', models.CharField(blank=True, max_length=100)),
                ('longitud', models.CharField(blank=True, max_length=100)),
                ('latitud', models.CharField(blank=True, max_length=100)),
                ('createdAt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
