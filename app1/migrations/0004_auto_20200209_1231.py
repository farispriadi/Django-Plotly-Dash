# Generated by Django 3.0.2 on 2020-02-09 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20200209_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='transaction_btc_quantity',
        ),
        migrations.RemoveField(
            model_name='account',
            name='transaction_date',
        ),
        migrations.RemoveField(
            model_name='account',
            name='transaction_total_usd_price',
        ),
        migrations.RemoveField(
            model_name='account',
            name='transaction_type',
        ),
        migrations.RemoveField(
            model_name='account',
            name='transaction_usd_price',
        ),
    ]
