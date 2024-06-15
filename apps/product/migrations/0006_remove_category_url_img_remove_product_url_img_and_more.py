# Generated by Django 5.0.6 on 2024-06-15 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_product_category_id_alter_product_promotion_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='url_img',
        ),
        migrations.RemoveField(
            model_name='product',
            name='url_img',
        ),
        migrations.RemoveField(
            model_name='promotion',
            name='url_img',
        ),
        migrations.AddField(
            model_name='category',
            name='img',
            field=models.ImageField(blank=True, max_length=250, upload_to='category/% Y/% m/% d/', verbose_name='img'),
        ),
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, max_length=250, upload_to='product/% Y/% m/% d/', verbose_name='img'),
        ),
        migrations.AddField(
            model_name='promotion',
            name='img',
            field=models.ImageField(blank=True, max_length=250, upload_to='promotion/% Y/% m/% d/', verbose_name='img'),
        ),
    ]
