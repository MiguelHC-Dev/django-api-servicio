# Generated by Django 4.2 on 2024-05-19 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_carrera_nombre_carrera'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviciosocial',
            name='area',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='serviciosocial',
            name='cargo_titular',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='serviciosocial',
            name='dependencia_organizacion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='serviciosocial',
            name='nombre_programa',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='serviciosocial',
            name='titular_organizacion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]