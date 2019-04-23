from . import getmovies,getphones,getweathers,view
import time
from crawler.models import Movies
from crawler.models import Weathers
from crawler.models import Phones
from django.shortcuts import render
from django.http import HttpResponse

def deletelall(request):
    context = {}
    try:
        Movies.objects.all().delete()
        Weathers.objects.all().delete()
        Phones.objects.all().delete()
        context['zhuangtai']='删除成功！'
    except:
        context['zhuangtai']='删除失败！'
    return render(request, 'zhuangtai.html', context)

def insertdata(request):
    context = {}
    try:
        getmovies.get_movies()
        time.sleep(2)
        getphones.get_phones('小米9')
        time.sleep(2)
        getweathers.get_weather()
        time.sleep(2)
        context['zhuangtai']='获取成功！'
    except:
        context['zhuangtai']='获取失败！'
    return render(request, 'zhuangtai.html', context)

def updatabase(request):
    deletelall(request)
    insertdata(request)
    context = {}
    context['zhuangtai']='更新成功！'
    return render(request, 'zhuangtai.html', context)

def search_phone(request):
    context = {}    
    if request.POST:
        context['phonename'] = request.POST['phonename']
    getphones.get_phones(context['phonename'])
    time.sleep(2)
    context['zhuangtai']=context['phonename']+'获取成功！'
    return render(request, 'zhuangtai.html', context)
    
