# Generated by Django 2.1.5 on 2019-03-02 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='支付时间'),
        ),
    ]
