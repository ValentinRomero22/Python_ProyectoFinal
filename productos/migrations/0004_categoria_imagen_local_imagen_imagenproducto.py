# Generated by Django 4.0.4 on 2022-06-30 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_producto_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='usuarios'),
        ),
        migrations.AddField(
            model_name='local',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='locales'),
        ),
        migrations.CreateModel(
            name='ImagenProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='productos')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
            ],
        ),
    ]