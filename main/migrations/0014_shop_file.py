# Generated by Django 4.2.5 on 2023-09-16 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_shop_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='file',
            field=models.FilePathField(blank=True, null=True, verbose_name='Файл с товарами'),
        ),
    ]