# Generated by Django 4.1.1 on 2022-09-11 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_inversion_horacreacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inversion',
            name='horaCreacion',
        ),
    ]
