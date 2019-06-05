from django.db import models

# Create your models here.
class Movies(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=10000)
    synopsis = models.CharField(max_length=10000)
    time = models.CharField(max_length=200)

    class Meta:
        verbose_name = '电影'
        verbose_name_plural = '电影'

class Weathers(models.Model):
    city = models.CharField(max_length=200)
    dates = models.CharField(max_length=200)
    winL = models.CharField(max_length=200)
    temperatureLow = models.CharField(max_length=200)
    temperatureHigh = models.CharField(max_length=200)
    weather = models.CharField(max_length=20)

    class Meta:
        verbose_name = '天气'
        verbose_name_plural = '天气'

class Phones(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=10000)
    price=models.CharField(max_length=200)
    time = models.CharField(max_length=200)

    class Meta:
        verbose_name = '手机'
        verbose_name_plural = '手机'

class User(models.Model):
    gender = (
        ('male','男'),
        ('female','女'),
    ) 
    name = models.CharField(max_length=128,unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32,choices=gender,default='男')
    c_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'