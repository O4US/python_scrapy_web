from django.db import models
from DjangoUeditor.models import UEditorField
from imagekit.models import ImageSpecField,ProcessedImageField
from imagekit.processors import ResizeToFill


# Create your models here.
class NewsType(models.Model):
    name = models.CharField('分类名称', max_length=10) 
    thumbnail = ProcessedImageField(upload_to='upimages/news/',processors=[ResizeToFill(1920, 600)],format='JPEG',options={'quality': 100},verbose_name='缩略图',default='upimages/products/default(2).jpg')
    text = models.TextField('简介',null=True)
    def __str__(self):
        return self.name 
    class Meta:
        verbose_name = '资讯类别'
        verbose_name_plural = '资讯类别'
 
 
class News(models.Model):
    name = models.CharField('文章标题', max_length=30)
    add_time = models.DateField('发布日期', auto_now = True)
    is_show = models.BooleanField('是否展示',default = True)
    news_type = models.ForeignKey(NewsType, verbose_name='文章分类', on_delete=models.CASCADE)
    content = UEditorField('文章内容',width='800',height='600',imagePath='upimages/',filePath='upfiles/')
    thumbnail = ProcessedImageField(upload_to='upimages/news/',processors=[ResizeToFill(64, 64)],format='JPEG',options={'quality': 100},verbose_name='缩略图',default='upimages/thumbnail/default.jpg')
    text = models.TextField('简介',null=True)
    def __str__(self):
        return self.name 
    class Meta:
        verbose_name = '新闻资讯'
        verbose_name_plural = '新闻资讯'

class ProductsType(models.Model):
    name = models.CharField('产品种类', max_length=10)
    thumbnail = models.ImageField('图片',upload_to='upimages/products/',blank = True, null = True,default='upimages/thumbnail/default.jpg')
    text = models.TextField('简介',null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '产品种类'
        verbose_name_plural = '产品种类'    

class Product(models.Model):    
    name = models.CharField('产品名称', max_length=10)
    add_time = models.DateField('发布日期', auto_now = True)
    is_show = models.BooleanField('是否展示',default = True)
    product_type = models.ForeignKey(ProductsType, verbose_name='产品种类', on_delete=models.CASCADE)    
    content = UEditorField('产品介绍',width='800',height='600',imagePath='product/',filePath='upfile/')
    thumbnail = ProcessedImageField(upload_to='upimages/products/',processors=[ResizeToFill(64, 64)],format='JPEG',options={'quality': 100},verbose_name='缩略图',default='upimages/thumbnail/default.jpg')
    text = models.TextField('简介',null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '产品介绍'
        verbose_name_plural = '产品介绍'


class User(models.Model):
    name = models.CharField('姓名', max_length=10)
    tel = models.CharField('手机号', max_length=20)
    sex = models.CharField('性别', max_length=10)
    question = models.TextField('咨询的内容',null=True,blank = True)
    is_quest = models.BooleanField('是否已联系',default = False,null=True)
    def __str__(self):
        if(self.is_quest):
            return self.name+' '+self.sex+' 已联系'
        else:
            return self.name+' '+self.sex+' 未联系'
    class Meta:
        verbose_name = '客户咨询'
        verbose_name_plural = '客户咨询'

class Imglist(models.Model):
    name = models.CharField('图片名称', max_length=50)
    text = models.TextField('简介',blank=True,null=True)
    imgurl = ProcessedImageField(upload_to='upimages/thumbnail/',processors=[ResizeToFill(1920, 600)],format='JPEG',options={'quality': 100},verbose_name='缩略图',default='upimages/products/default(2).jpg')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '轮播图片'
        verbose_name_plural = '轮播图片'

class About(models.Model):
    content = UEditorField('关于我们',width='800',height='600',imagePath='images/',filePath='upfile/')
    def __str__(self):
        return '关于我们'+str(self.id)
    class Meta:
        verbose_name = '关于我们'
        verbose_name_plural = '关于我们'    