# Generated by Django 4.1.5 on 2023-02-06 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0007_rename_nomcarrera_carrera_carrera'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entregable',
            old_name='entrega',
            new_name='entregado',
        ),
    ]