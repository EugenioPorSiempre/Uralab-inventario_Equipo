# Generated by Django 3.2 on 2021-05-07 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invent_equipo', '0002_auto_20210507_0103'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipo',
            old_name='detalle',
            new_name='nombre',
        ),
    ]
