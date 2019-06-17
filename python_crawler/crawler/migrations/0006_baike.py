# Generated by Django 2.1.7 on 2019-06-17 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0005_auto_20190618_0231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Baike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=200)),
                ('depth', models.CharField(max_length=200)),
                ('fhurl', models.CharField(max_length=10000)),
                ('churl', models.CharField(max_length=10000)),
                ('time', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': '百科',
                'verbose_name_plural': '百科',
            },
        ),
    ]
