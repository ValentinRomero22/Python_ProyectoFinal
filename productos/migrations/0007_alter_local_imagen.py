# Generated by Django 4.0.4 on 2022-07-03 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0006_alter_imagenproducto_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='local',
            name='imagen',
            field=models.ImageField(blank=True, default='../static/sin_imagen.png', null=True, upload_to='locales'),
        ),
    ]
