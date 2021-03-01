# Generated by Django 2.1.7 on 2020-04-28 06:54

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_auto_20200428_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imglist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='图片名称')),
                ('text', models.TextField(blank=True, null=True, verbose_name='简介')),
                ('imgurl', imagekit.models.fields.ProcessedImageField(default='upimages/products/default(2).jpg', upload_to='upimages/thumbnail/', verbose_name='缩略图')),
            ],
            options={
                'verbose_name': '轮播图片',
                'verbose_name_plural': '轮播图片',
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='add_time',
            field=models.DateField(auto_now=True, verbose_name='发布日期'),
        ),
    ]