# Generated by Django 4.0.6 on 2023-02-19 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='countInStocks',
            new_name='countInStock',
        ),
    ]