# Generated by Django 4.1.1 on 2022-09-11 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_inversion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inversion',
            old_name='producto_id',
            new_name='producto',
        ),
    ]
