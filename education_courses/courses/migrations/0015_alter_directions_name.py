# Generated by Django 4.2.1 on 2023-06-01 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_directions_image_alter_directions_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directions',
            name='name',
            field=models.CharField(choices=[('Информационные технологии', 'Информационные технологиий'), ('Маркетинг', 'Маркетинг'), ('Дизайн', 'Дизайн')], max_length=50, verbose_name='Языки программирования'),
        ),
    ]