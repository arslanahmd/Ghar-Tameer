# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-16 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_auto_20160207_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliverygroup',
            name='status',
            field=models.CharField(choices=[(b'new', 'Processing'), (b'cancelled', 'Cancelled'), (b'shipped', 'Shipped'), (b'payment-pending', 'Payment pending'), (b'fully-paid', 'Fully paid')], default=b'new', max_length=32, verbose_name='delivery status'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[(b'new', 'Processing'), (b'cancelled', 'Cancelled'), (b'shipped', 'Shipped'), (b'payment-pending', 'Payment pending'), (b'fully-paid', 'Fully paid')], default=b'new', max_length=32, verbose_name='order status'),
        ),
        migrations.AlterField(
            model_name='orderhistoryentry',
            name='status',
            field=models.CharField(choices=[(b'new', 'Processing'), (b'cancelled', 'Cancelled'), (b'shipped', 'Shipped'), (b'payment-pending', 'Payment pending'), (b'fully-paid', 'Fully paid')], max_length=32, verbose_name='order status'),
        ),
    ]
