from django.contrib import admin
from backend.models import *
# Register your models here.
admin.site.site_header = '雨菲后台管理平台'
admin.site.site_title = '雨菲后台管理平台'

admin.site.register(NewsType)
admin.site.register(News)
admin.site.register(ProductsType)
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Imglist)
admin.site.register(About)