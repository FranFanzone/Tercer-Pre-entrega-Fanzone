# Generated by Django 4.1.5 on 2023-02-05 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entregable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia', models.CharField(max_length=40)),
                ('entrega', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='carrera',
            name='entregables',
        ),
    ]
