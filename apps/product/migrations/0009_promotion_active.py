# Generated by Django 5.0.6 on 2024-06-24 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_category_options_alter_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
