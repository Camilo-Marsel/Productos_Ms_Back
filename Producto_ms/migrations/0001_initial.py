# Generated by Django 3.2.7 on 2021-11-22 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField(default=0)),
                ('precio', models.IntegerField(default=0)),
                ('descripcion', models.TextField(blank=True, max_length=2000)),
            ],
        ),
    ]
