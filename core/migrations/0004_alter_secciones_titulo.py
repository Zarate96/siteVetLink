# Generated by Django 4.2.1 on 2023-07-28 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_slide_nombre_alter_elementosnavbar_is_button'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secciones',
            name='titulo',
            field=models.TextField(verbose_name='Texto principal'),
        ),
    ]