# Generated by Django 4.2.1 on 2023-05-26 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Индивидуальные занятия', 'Индивидуальные занятия'), ('Диплом установленного образца', 'Диплом установленного образца'), ('Гарантия трудоустройства', 'Гарантия трудоустройства'), ('Профориентация', 'Профориентация')], max_length=150, verbose_name='Опция')),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Базовый', 'Базовый'), ('Мастер', 'Мастер'), ('Про', 'Про')], max_length=50, verbose_name='Пакет')),
            ],
        ),
        migrations.CreateModel(
            name='Temp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Стандартный', 'Стандартный'), ('Интенсивный', 'Интенсивный'), ('Замедленный', 'Замедленный')], max_length=50, verbose_name='Темп')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='directions',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.directions', verbose_name='Направления'),
        ),
        migrations.AddField(
            model_name='order',
            name='option',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.option', verbose_name='Опции'),
        ),
        migrations.AddField(
            model_name='order',
            name='package',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.package', verbose_name='Пакет'),
        ),
        migrations.AddField(
            model_name='order',
            name='temp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.temp', verbose_name='Темп обучения'),
        ),
    ]
