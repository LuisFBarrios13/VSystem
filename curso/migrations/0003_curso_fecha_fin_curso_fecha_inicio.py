# Generated by Django 5.1.1 on 2024-09-30 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0002_remove_curso_duracion_remove_curso_fecha_fin_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='fecha_fin',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='curso',
            name='fecha_inicio',
            field=models.DateField(blank=True, null=True),
        ),
    ]
