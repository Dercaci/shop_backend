# Generated by Django 4.0.1 on 2022-02-02 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0002_product_number_of_wishes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='number_of_wishes',
        ),
    ]