from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.db.models import Q

from backend.models import *
from backend.serializers import *

#Create your views here.
class GetNewsById(APIView):
    def get(self, request,id):
        queryset=News.objects.filter(id=id,is_show=True)
        serializer = NewsSl(queryset, many=True)#序列化
        return Response(serializer.data)

class GetAllNews(APIView):
    def get(self, request):
        queryset=News.objects.filter(is_show=True)
        serializer = NewsSl(queryset, many=True)
        return Response(serializer.data)

class GetNewsListByType(APIView):
    def get(self, request,news_type):
        queryset=News.objects.filter(news_type=news_type,is_show=True)
        serializer = NewsSl(queryset, many=True)
        return Response(serializer.data)

class GetAllNewsType(APIView):
    def get(self, request):
        queryset=NewsType.objects.all()
        serializer = NewsTypeSl(queryset, many=True)
        return Response(serializer.data)     

class GetAllProductsType(APIView):
    def get(self, request):
        queryset=ProductsType.objects.all()
        serializer = ProductsTypeSl(queryset, many=True)
        return Response(serializer.data)     

class GetProductsListByType(APIView):
    def get(self,request,product_type):
        queryset=Product.objects.filter(product_type=product_type,is_show=True)
        serializer = ProductSl(queryset,many=True)
        return Response(serializer.data)

class GetProductById(APIView):
    def get(self, request,id):
        queryset=Product.objects.filter(id=id,is_show=True)
        serializer = ProductSl(queryset, many=True)
        return Response(serializer.data)

class PostUserInfo(APIView):
    def post(self,request):
        serializer = UserSl(data=request.data)
        if(serializer.is_valid()):
            serializer.save()        
            msg='提交成功！我们将会在24小时之内回复您'
        else:
            msg='提交失败！'+str(serializer.errors)
            serializer.validated_data
        return Response({'message':msg})

class GetAllImgList(APIView):
    def get(self,request):
        queryset=Imglist.objects.all()
        serializer=ImglistSl(queryset,many=True)
        return Response(serializer.data)

class GetAboutUs(APIView):
    def get(self,request):
        queryset=About.objects.all()
        serializer=AboutSl(queryset,many=True) 
        return Response(serializer.data)