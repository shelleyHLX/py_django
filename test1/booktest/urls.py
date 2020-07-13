
from django.conf.urls import url
from .views import *
# import views

urlpatterns = [
    url('^index/$', index),
    url('^(\d+)/$', detail)
]
