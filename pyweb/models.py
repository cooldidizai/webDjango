from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ArticlePost(models.Model):
    # 文章作者。
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # 文章标题。
    title = models.CharField(max_length=100)

    # 文章正文。
    body = models.TextField()

    # 文章创建时间和最后一次修改时间。
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        # ordering 指定模型返回的数据的排列顺序。
        # '-created' 表明数据应该以倒序排列。
        ordering = ('-created',)

    def __str__(self):
        # 返回文章标题。
        return self.title