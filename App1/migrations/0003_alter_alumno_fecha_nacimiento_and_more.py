# Generated by Django 4.1.5 on 2023-02-06 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0002_entregable_remove_carrera_entregables'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='fecha_nacimiento',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='fecha_nacimiento',
            field=models.DateField(),
        ),
    ]
