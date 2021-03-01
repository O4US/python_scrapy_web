from rest_framework import serializers
from backend.models import *

class NewsSl(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id','name','add_time','news_type','content','thumbnail','text')

class NewsTypeSl(serializers.ModelSerializer):
    class Meta:
        model = NewsType
        fields = ('id','name','thumbnail','text')

class ProductsTypeSl(serializers.ModelSerializer):
    class Meta:
        model = ProductsType
        fields = ('id','name','thumbnail','text')

class ProductSl(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name','add_time','product_type','content','thumbnail','text')

class UserSl(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name','tel','sex','question')

class ImglistSl(serializers.ModelSerializer):
    class Meta:
        model = Imglist
        fields = ('id','name','text','imgurl')

class AboutSl(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('id','content')