# Generated by Django 4.2.5 on 2023-09-10 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_parameter_productparameter_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameter',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Название'),
        ),
    ]