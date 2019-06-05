from django.shortcuts import render
from django.http import HttpResponse
from crawler.models import Movies
from crawler.models import Weathers
from crawler.models import Phones
from django.db.models import Q
def index(request):
    context = {}
    context['zhuangtai']='Hello！'
    return render(request, 'index.html', context)
 
def movies(request):
    movies=Movies.objects.all()
    return render(request, 'movies.html', {'movies': movies})

def weathers(request):
    weathers=Weathers.objects.all()
    return render(request, 'weathers.html', {'weathers': weathers})

def phones(request):
    phones=Phones.objects.all()
    return render(request, 'phones.html', {'phones': phones})

def insertsearch(request):
    return render(request, 'insertsearch.html')

def phonesearch(request):
    context = {}
    if request.POST:
        context['val'] = request.POST['val']
    phones=Phones.objects.filter(Q(name__icontains=context['val'])|Q(price__icontains=context['val'])|Q(time__icontains=context['val']))
    return render(request, 'phones.html', {'phones': phones,'history':context['val']})

def moviesearch(request):
    context = {}
    if request.POST:
        context['val'] = request.POST['val']
    movies=Movies.objects.filter(Q(name__icontains=context['val'])|Q(synopsis__icontains=context['val'])|Q(time__icontains=context['val']))
    return render(request, 'movies.html', {'movies': movies,'history':context['val']})

def weathersearch(request):
    context = {}
    if request.POST:
        context['val'] = request.POST['val']
    weathers=Weathers.objects.filter(Q(city__icontains=context['val'])|Q(dates__icontains=context['val'])|Q(winL__icontains=context['val'])\
    |Q(temperatureLow__icontains=context['val'])|Q(temperatureHigh__icontains=context['val'])|Q(weather__icontains=context['val']))
    return render(request, 'weathers.html', {'weathers': weathers,'history':context['val']})

def login(request):
    return render(request, 'login.html')

def regist(request):
    return render(request, 'regist.html')

def control(request):
    return render(request, 'control.html')