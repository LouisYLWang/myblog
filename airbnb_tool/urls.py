# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

app_name = 'Airbnb_tools'
urlpatterns = [
    url(r'airbnb_tool', views.index, name='index'),
    url(r'airbnb_tool_result', views.result, name='result'),
]

