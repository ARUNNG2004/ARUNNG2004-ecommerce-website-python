# Generated by Django 5.1.1 on 2024-09-22 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0002_remove_product_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.ImageField(null=True, upload_to='imgaes/'),
        ),
    ]