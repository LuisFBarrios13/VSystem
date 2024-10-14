# Generated by Django 5.1.1 on 2024-10-14 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matricula',
            name='estado',
            field=models.CharField(choices=[('Activo', 'Activo'), ('Suspendido', 'Suspendido'), ('Finalizado', 'Finalizado')], default='Activo', max_length=150),
        ),
    ]
