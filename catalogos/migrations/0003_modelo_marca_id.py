# Generated by Django 3.2 on 2021-05-07 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0002_color_estado_marca_modelo'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelo',
            name='marca_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='catalogos.marca'),
            preserve_default=False,
        ),
    ]
