# Generated by Django 2.1.7 on 2019-06-05 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0002_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movies',
            options={'verbose_name': '电影', 'verbose_name_plural': '电影'},
        ),
        migrations.AlterModelOptions(
            name='phones',
            options={'verbose_name': '手机', 'verbose_name_plural': '手机'},
        ),
        migrations.AlterModelOptions(
            name='weathers',
            options={'verbose_name': '天气', 'verbose_name_plural': '天气'},
        ),
    ]
