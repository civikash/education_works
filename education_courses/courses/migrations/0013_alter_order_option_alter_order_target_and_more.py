# Generated by Django 4.2.1 on 2023-06-01 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_remove_order_option_remove_order_target_order_option_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='option',
            field=models.ManyToManyField(to='courses.option', verbose_name='Опции'),
        ),
        migrations.AlterField(
            model_name='order',
            name='target',
            field=models.ManyToManyField(to='courses.target', verbose_name='Цели'),
        ),
        migrations.AlterField(
            model_name='order',
            name='value',
            field=models.FloatField(null=True, verbose_name='Сумма'),
        ),
    ]
