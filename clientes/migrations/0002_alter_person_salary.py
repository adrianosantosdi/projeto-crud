# Generated by Django 5.0.4 on 2024-10-10 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='salary',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
