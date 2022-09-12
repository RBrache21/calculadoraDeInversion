# Generated by Django 4.1.1 on 2022-09-11 22:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_inversion_fechacreacion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inversion',
            name='fechaCreacion',
        ),
        migrations.RemoveField(
            model_name='inversion',
            name='horaCreacion',
        ),
        migrations.AddField(
            model_name='inversion',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]