# Generated by Django 4.1.3 on 2023-01-04 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=80)),
                ('apellido', models.CharField(max_length=80)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('correo', models.EmailField(max_length=100, unique=True)),
                ('ubicacion', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
            ],
        ),
    ]