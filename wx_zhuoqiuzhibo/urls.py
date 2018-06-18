from django.conf.urls import url
from django.views.generic import TemplateView

import wx_zhuoqiuzhibo.views as views

urlpatterns = [
    url(r'^snkrank/$', views.SnkRank.as_view(), name='snkrank'),
    url(r'^ranktable/$', views.ranktable, name='ranktable')
]