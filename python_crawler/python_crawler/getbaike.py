import requests
import re 
import time
from crawler.models import Baike
from urllib.request import quote, unquote

exist_url=[]
g_writecount=0
staticurl="https://baike.baidu.com/item/"
def scrapy(url,maxdepth,depth):
    print("调用一次")
    global g_writecount
    try:
        headers={'User-Agent':'Mozilla/5.0(Windows;U;Windows NT 6.1;en-US;rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
        r=requests.get(staticurl+url,headers=headers)
        r.encoding='UTF-8'
        html=r.text
    except Exception as e:
        print('Failed',url)
        print(e)
        exist_url.append(url)
        return None
    exist_url.append(url)
    link_list=re.findall('<a target.*? href="/item/([^:#=<>?]*?)".*?</a>',html)
    unique_list=list(set(link_list)-set(exist_url))
    for eachone in unique_list:
        eachone=unquote(eachone)
        g_writecount+=1
        #output="No."+str(g_writecount)+"\t Depth:"+str(depth)+"\t"+url+'->'+eachone+'\n'
        #print(output)
        #with open('title.txt',"a+",encoding='UTF-8') as f:
        #    f.write(output)
        #    f.close()
        now=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        record=Baike(num="No."+str(g_writecount),depth="Depth:"+str(depth),fhurl=staticurl+url,churl=staticurl+eachone,time=now)
        record.save()
        if depth<maxdepth:
            scrapy(eachone,depth+1,maxdepth)

def getbaike(name,maxdepth,depth):
    exist_url.clear()
    global g_writecount
    g_writecount=0
    time1=time.time()   
    scrapy(name,maxdepth,depth)
    time2=time.time()    
    return name+"获取完成,耗时:"+str(time2-time1)+"秒"