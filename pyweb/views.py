from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import ArticlePost
list = [{"name":'python',"function":'nice'},{"name":'web',"function":'good'}]
def index(request):
    name = request.POST.get('name',None)
    password = request.POST.get('function',None)

    data= {'name':name,'function':password}
    list.append(data)
    return render(request,'index.html',
                  {"form":list})
def article_list(requset):
    articles = ArticlePost.objects.all()
    context ={'articles':articles}
    return render (requset,'article/list.html',context)
def zhuye(request):
    return render(request,'zhuye.html')