# Generated by Django 3.0.8 on 2020-08-04 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200803_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(default='Мужской', max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='get_notifications',
            field=models.BooleanField(default=False, verbose_name='Получать уведомления'),
        ),
    ]
