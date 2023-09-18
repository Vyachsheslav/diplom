# Generated by Django 4.2.5 on 2023-09-11 11:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0011_alter_shop_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shop', to=settings.AUTH_USER_MODEL, verbose_name='Владелец магазина'),
        ),
    ]
