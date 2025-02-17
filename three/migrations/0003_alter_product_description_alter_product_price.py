# Generated by Django 5.1.3 on 2024-12-17 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('three', '0002_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
