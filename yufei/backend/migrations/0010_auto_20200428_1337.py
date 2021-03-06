# Generated by Django 2.1.7 on 2020-04-28 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_quest',
            field=models.BooleanField(default=False, null=True, verbose_name='是否已联系'),
        ),
        migrations.AlterField(
            model_name='user',
            name='question',
            field=models.TextField(blank=True, null=True, verbose_name='咨询的内容'),
        ),
    ]
