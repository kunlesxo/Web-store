# Generated by Django 5.1.5 on 2025-01-22 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_imagefiled_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='images',
        ),
    ]
