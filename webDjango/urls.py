"""
URL configuration for webDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from pyweb import views # 导入views模块
urlpatterns = [
    path('admin/',admin.site.urls),
    path('index/',views.index, name='index'), # 配置当访问index时去调用views下的index方法
    path('article-list/',views.article_list,name='article_list'),
    path('zhuye/',views.zhuye,name='zhuye'),
]
