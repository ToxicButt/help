# Generated by Django 4.1.5 on 2023-04-06 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_cart_cart_id_alter_cart_created_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartitem',
            options={'verbose_name': 'элемент карзины', 'verbose_name_plural': 'элементы карзин'},
        ),
    ]
