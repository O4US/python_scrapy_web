django+bootstrap一个Python爬虫网页
====
页面效果预览 www.personweb.net

已完成:
* 爬取豆瓣前250部电影
* 部分地区天气
* 京东手机

未完成:
* 优化爬虫速度
* 用户登录注册
* 管理员登录与控制页面
* 页面内容分页显示
* 页面加载进度条动画效果
* 页面内容局部加载显示Ajax

## 安装说明:

基于Python3.6.6 win64,安装库:request,django2.1.7,bs4,selenium,lxml,urllib<br>
MySQL5.7 win64<br>
django\python_crawler\python_crawler\Chromedriver.exe版本需要与本机Chrome浏览器版本一致<br>
当前Chromedriver.exe版本为73.0.3683<br>

### 1.Chromedriver
下载地址http://npm.taobao.org/mirrors/chromedriver<br>

### 2.MySQL编码配置
默认位置C:\ProgramData\MySQL\MySQL Server 5.7\my.ini<br>
* 在[client]后添加<br>
```default-character-set = utf8```<br>
* 在[mysql]后添加<br>
```default-character-set = utf8```<br>
* 在[mysqld]后添加<br>
```character-set-server=utf8```<br>
保存并重启MySQL服务<br>

### 3.请修改setting.py
位于django\python_crawler\python_crawler\settings.py<br>
```DEBUG = False``` #调试模式已关闭,如需开启请修改为True<br>
数据库连接配置,数据库名需对应MySQL数据库<br>
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'python_crawler', #数据库名
        'USER': 'sa', #用户名
        'PASSWORD': '1234', #密码
        'HOST':'localhost', #地址
        'PORT':'3306', #端口
    }
}
```
保存setting.py<br>

### 4.使用cmd,cd到项目路径下
PS C:\Users\用户> ```cd D:\developitems\django\python_crawler```<br>
或者先执行 ```d:```<br>
切换磁盘再执行```cd D:\developitems\django\python_crawler```<br>
然后执行<br>
```python manage.py makemigrations crawler```<br>
```python manage.py migrate crawler```<br>
```python manage.py migrate```<br>
后MySQL的表结构就创建完成了<br>

### 5.调试运行
```python manage.py runserver 本机ip+端口号 --insecure```<br>
例如:```python manage.py runserver 127.0.0.1:88 --insecure```<br>
出现<br>
    Django version 2.1.7, using settings 'python_crawler.settings'<br>
    Starting development server at http://。。。。:88/<br>
    Quit the server with CTRL-BREAK.<br>
后可以通过本机ip+端口号再局域网内访问项目<br>