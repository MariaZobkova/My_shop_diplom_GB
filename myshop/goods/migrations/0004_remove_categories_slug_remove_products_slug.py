# Generated by Django 5.0.3 on 2024-04-13 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='products',
            name='slug',
        ),
    ]
