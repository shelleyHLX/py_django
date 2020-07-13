
import sys

from django.contrib import admin

sys.path.append("/home/hlx2/py_djan/test1/booktest/models")
# import models
from .models import *   # python3
# from models import *  # py2


# 修改增加数据的名称改变
class BookInfoAdmin(admin.ModelAdmin):
    # 模型类的字段
    list_display = ['id','title','pub_date']

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id','name','content','gender','book']

# Register your models here.

admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)



