from . import getmovies,getphones,getweathers,view,sign12306,getbaike
import time
from crawler.models import Movies,Weathers,Phones,User,Baike
from django.shortcuts import render
from django.http import HttpResponse

def deletelall(request):   
    context = {}
    username=request.session.get('username')
    context['username']=username
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
    username=request.session.get('username')
    context['username']=username
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
    username=request.session.get('username')
    context['username']=username
    context['zhuangtai']='更新成功！'
    return render(request, 'zhuangtai.html', context)

def search_phone(request):
    context = {}
    username=request.session.get('username')
    context['username']=username    
    if request.POST:
        context['phonename'] = request.POST['phonename']
    getphones.get_phones(context['phonename'])
    time.sleep(2)
    context['zhuangtai']=context['phonename']+'获取成功！'
    return render(request, 'zhuangtai.html', context)

def login(request):
    userinfo={}
    context = {}
    if request.POST:
        userinfo['username'] = request.POST['Username']
        userinfo['password'] = request.POST['Password']                
    user=User.objects.filter(name=userinfo['username'],password=userinfo['password'])
    if user:
        request.session['username']=userinfo['username']
        request.session['password']=userinfo['password']
        return render(request, 'index.html', userinfo)
    else:              
        context['zhuangtai']='用户名或密码错误！'
        return render(request, 'zhuangtai.html', context)

def regist(request):
    userinfo={}
    context = {}
    if request.POST:
        userinfo['username'] = request.POST['Username']
        userinfo['password'] = request.POST['Password']
        userinfo['email'] = request.POST['Email']
    user=User.objects.filter(name=userinfo['username'])
    if user:
        context['zhuangtai']='该用户已存在！'
        return render(request, 'zhuangtai.html', context)
    else:
        request.session['username']=userinfo['username']
        request.session['password']=userinfo['password']
        now=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        record=User(name=userinfo['username'],password=userinfo['password'],email=userinfo['email'],sex='男',c_time=now)
        record.save()
        return render(request, 'index.html', userinfo)

def unlogin(request):
    if request.session['username']!=None and request.session['password']!=None:
        del request.session['username']
        del request.session['password']
    return render(request, 'index.html')

def login12306(request):
    username=request.session.get('username',None)
    password=request.session.get('password',None)
    sign12306.Demo(username,password)()
    context = {}
    username=request.session.get('username')
    context['username']=username
    context['zhuangtai']='未判断验证结果！'
    return render(request, 'zhuangtai.html', context)

def baike_search(request):
    context = {}
    username=request.session.get('username')
    context['username']=username    
    if request.POST:
        context['value'] = request.POST['value']
        context['depth'] = request.POST['depth']
    try:
        depth=int(context['depth'])
        Baike.objects.all().delete()
        costime=getbaike.getbaike(context['value'],depth,1)
        baike=Baike.objects.all()
        return render(request, 'baike.html', {'baike': baike,'costime':costime,'username':username})
    except:
        context['zhuangtai']='深度请输入整数且最好小于5！'
        return render(request, 'zhuangtai.html', context)