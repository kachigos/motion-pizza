# Generated by Django 4.0.3 on 2022-04-09 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iPizza', '0008_stock_alter_ordermain_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermain',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Цена'),
        ),
    ]