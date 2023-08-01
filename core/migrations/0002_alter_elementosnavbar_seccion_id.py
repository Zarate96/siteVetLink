# Generated by Django 4.2.1 on 2023-07-28 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementosnavbar',
            name='seccion_id',
            field=models.CharField(blank=True, choices=[('inicio', 'inicio'), ('proceso', 'proceso'), ('video', 'video'), ('contacto', 'contacto')], max_length=100, verbose_name='Nombre de sección'),
        ),
    ]