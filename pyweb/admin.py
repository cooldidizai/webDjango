from django.contrib import admin
from .models import ArticlePost

# 注册 ArticlePost 到后台管理。
admin.site.register(ArticlePost)