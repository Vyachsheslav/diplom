# Generated by Django 4.2.5 on 2023-09-11 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_order_contact_alter_order_state_orderitem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='dt',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время совершения заказа'),
        ),
    ]
