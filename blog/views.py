# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from . import models
'''
def index(request):
    context = {'w':'wanglinlin', 'h':'houweilin'}
    #context['hello'] = 'Hello World!'
    return render(request, 'index.html', context)
'''

def index(request):
    article = models.Article.objects.get(pk=2)
    return render(request,'index.html', {'article':article})