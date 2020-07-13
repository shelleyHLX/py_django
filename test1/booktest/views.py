# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.

# HttpRequest,请求作为视图，必须返回响应
# def index(request,):
#     # HttpResponse
#     return HttpResponse('<h1>hello word</h1>')

#
# def index(request):
#     # HttpResponse
#     context = {'title':"django首页", 'list':range(10)}
#
#     return render(request, 'booktest/index.html',context)


def index(request):
    # HttpResponse
    list = BookInfo.objects.all()
    # BookInfo.
    context = {'booklist':list}
    return render(request, 'booktest/index2.html',context)

# '^(\d+)/$'，一个()提取一个变量
# /home/hlx2/py_djan/test1/booktest/urls.py
def detail(request,id):
    list = BookInfo.objects.get(id=id).heroinfo_set.all()
    context = {'herolist':list}
    return render(request, 'booktest/detail.html', context)
