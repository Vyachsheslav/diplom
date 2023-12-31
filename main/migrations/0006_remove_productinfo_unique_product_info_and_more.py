# Generated by Django 4.2.5 on 2023-09-10 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_price_rrc_productinfo_recommended_price_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='productinfo',
            name='unique_product_info',
        ),
        migrations.RemoveField(
            model_name='productinfo',
            name='external_id',
        ),
        migrations.AddConstraint(
            model_name='productinfo',
            constraint=models.UniqueConstraint(fields=('product', 'shop'), name='unique_product_info'),
        ),
    ]
