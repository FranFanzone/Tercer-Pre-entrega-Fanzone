# Generated by Django 4.1.5 on 2023-02-06 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0008_rename_entrega_entregable_entregado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carrera',
            old_name='carrera',
            new_name='nombre',
        ),
    ]