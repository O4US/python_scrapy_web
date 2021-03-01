from django.urls import path, re_path
from . import views

# app url 配置
urlpatterns = [
    #news
    path('getnewsbyid/<int:id>/', views.GetNewsById.as_view(),name='getnewsbyid'),
    path('getnewslistbytype/<int:news_type>/', views.GetNewsListByType.as_view(),name='getnewslistbytype'),
    path('getallnews/', views.GetAllNews.as_view(),name='getallnews'),
    path('getallnewstype/', views.GetAllNewsType.as_view(),name='getallnewstype'),
    #product
    path('getallproductstype/', views.GetAllProductsType.as_view(),name='getallproductstype'),
    path('getproductslistbytype/<int:product_type>/', views.GetProductsListByType.as_view(),name='getproductslistbytype'),
    path('getproductbyid/<int:id>/', views.GetProductById.as_view(),name='getproductbyid'),
    #user
    path('postuserinfo/', views.PostUserInfo.as_view(),name='postuserinfo'),
    #imglist
    path('getallimglist/',views.GetAllImgList.as_view(),name='getallimglist'),
    #aboutus
    path('getaboutus/',views.GetAboutUs.as_view(),name='getaboutus'),
]