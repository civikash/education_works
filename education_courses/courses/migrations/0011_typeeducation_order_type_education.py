# Generated by Django 4.2.1 on 2023-06-01 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_target_order_target'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90, verbose_name='Тип обучения')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='type_education',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.typeeducation', verbose_name='Тип обучения'),
        ),
    ]
