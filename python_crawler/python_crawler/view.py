from django.shortcuts import render
from django.http import HttpResponse
from crawler.models import Movies
from crawler.models import Weathers
from crawler.models import Phones
from django.db.models import Q
from . import control
def index(request):
    context = {}
    context['zhuangtai']='Hello！'
    context['myclass1']='active'
    username=request.session.get('username')
    context['username']=username
    return render(request, 'index.html', context)
 
def movies(request):
    username=request.session.get('username')
    movies=Movies.objects.all()    
    return render(request, 'movies.html', {'movies': movies,'myclass2':'active','username':username})

def weathers(request):
    username=request.session.get('username')
    weathers=Weathers.objects.all()
    return render(request, 'weathers.html', {'weathers': weathers,'myclass3':'active','username':username})

def phones(request):
    username=request.session.get('username')
    phones=Phones.objects.all()
    return render(request, 'phones.html', {'phones': phones,'myclass4':'active','username':username})

def insertsearch(request):
    username=request.session.get('username')
    return render(request, 'insertsearch.html',{'username':username})

def phonesearch(request):
    username=request.session.get('username')
    context = {}
    if request.POST:
        context['val'] = request.POST['val']
    phones=Phones.objects.filter(Q(name__icontains=context['val'])|Q(price__icontains=context['val'])|Q(time__icontains=context['val']))
    return render(request, 'phones.html', {'phones': phones,'history':context['val'],'username':username})

def moviesearch(request):
    username=request.session.get('username')
    context = {}
    if request.POST:
        context['val'] = request.POST['val']
    movies=Movies.objects.filter(Q(name__icontains=context['val'])|Q(synopsis__icontains=context['val'])|Q(time__icontains=context['val']))
    return render(request, 'movies.html', {'movies': movies,'history':context['val'],'username':username})

def weathersearch(request):
    username=request.session.get('username')
    context = {}
    if request.POST:
        context['val'] = request.POST['val']
    weathers=Weathers.objects.filter(Q(city__icontains=context['val'])|Q(dates__icontains=context['val'])|Q(winL__icontains=context['val'])\
    |Q(temperatureLow__icontains=context['val'])|Q(temperatureHigh__icontains=context['val'])|Q(weather__icontains=context['val']))
    return render(request, 'weathers.html', {'weathers': weathers,'history':context['val'],'username':username})

def login(request):
    return render(request, 'login.html')

def regist(request):
    return render(request, 'regist.html')

def control(request):
    return render(request, 'control.html')