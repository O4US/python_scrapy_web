"""yufei URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),  
    #配置富文本编辑器 
    path('ueditor/',include('DjangoUeditor.urls')),
    #连接后台接口
    path('api/', include('backend.urls')),
    #指向前端Vue.js框架
    re_path(r'^$', TemplateView.as_view(template_name="index.html")),
]
