# Generated by Django 4.2.1 on 2023-05-28 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_option_price_temp_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='value',
            field=models.IntegerField(null=True, verbose_name='Сумма'),
        ),
    ]