# Generated by Django 4.2.5 on 2023-09-10 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_contact_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.contact', verbose_name='Контактая информация'),
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(choices=[('basket', 'В корзине'), ('new', 'Новый'), ('confirmed', 'Подтвержден'), ('assembled', 'Собран'), ('sent', 'Отправлен'), ('delivered', 'Доставлен'), ('canceled', 'Отменен')], max_length=15, verbose_name='Статус'),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
                ('order', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='ordered_items', to='main.order', verbose_name='Заказ')),
                ('product_info', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='ordered_items', to='main.productinfo', verbose_name='Информация о товаре')),
            ],
            options={
                'verbose_name': 'Позиция в заказе',
                'verbose_name_plural': 'Список позиций в заказах',
            },
        ),
        migrations.AddConstraint(
            model_name='orderitem',
            constraint=models.UniqueConstraint(fields=('order_id', 'product_info'), name='unique_order_item'),
        ),
    ]