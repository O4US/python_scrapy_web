"""
Django settings for yufei project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#关闭url末尾自动添加/
#APPEND_SLASH=False

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u^vddjc4#%a4f%o0=#(a3zdxsq)gqevjvz-l84)v_t%wn2pgrs'

# SECURITY WARNING: don't run with debug turned on in production!

# 调试模式
DEBUG = True

ALLOWED_HOSTS = ['*',]


# Application definition

INSTALLED_APPS = [
    'simpleui',                       # admin美化
    'rest_framework',                 # RESTful接口    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'DjangoUeditor',                  # 富文本编辑器
    'imagekit',                       # 图片处理
    'backend',                        # 后端项目APP
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 解决跨域
    'corsheaders.middleware.CorsMiddleware',  
    #
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  #csrf验证
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# 解决跨域
CORS_ORIGIN_ALLOW_ALL = True
#开启服务器信息
SIMPLEUI_HOME_INFO = True
#开启使用分析
SIMPLEUI_ANALYSIS =True

ROOT_URLCONF = 'yufei.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['frontend/dist'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'yufei.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #数据库驱动
        'NAME': 'yufei', # 数据库名
        'USER': 'sa', # 用户名
        'PASSWORD': '1234', # 密码
        'HOST':'localhost', # 服务器
        'PORT':'3306', # 端口
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans' # 语言

TIME_ZONE = 'Asia/Shanghai' # 时间

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

# 静态文件优先使用项目路径
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, "frontend/dist/static"),)

# 媒体文件路径
MEDIA_URL = '/static/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "frontend/dist/static/media")