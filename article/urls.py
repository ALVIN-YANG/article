# -*- coding: utf-8 -*-
__author__ = 'ylq'
__date__ = '2020/2/4 5:46 下午'

from django.urls import path
from . import views

urlpatterns = [
    path('article/<code>', views.article, name='article'),

]
