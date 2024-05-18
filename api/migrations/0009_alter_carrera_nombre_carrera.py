# Generated by Django 4.2 on 2024-05-17 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_serviciosocial_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrera',
            name='nombre_carrera',
            field=models.CharField(choices=[('ISC', 'Ingeniería en Sistemas Computacionales'), ('CP', 'Contador Público'), ('IGE', 'Ingeniería en Gestión Empresarial'), ('II', 'Ingeniería Informática'), ('IC', 'Ingeniería Civil')], default='ISC', max_length=50),
        ),
    ]
