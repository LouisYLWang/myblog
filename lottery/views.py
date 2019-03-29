# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
from django.shortcuts import render
from django.http import HttpResponse
import time
 



# Create your views here.

def index(request):

    if request.method == 'GET': 
        lottery_num = random.randint(0,9999)
        context = {'lottery_num': lottery_num}
        return render(request, 'blog/lottery.html', context=context)
        


'''
def index(request):
    localtime = time.asctime( time.localtime(time.time()) )
    lottery_num = [random.randint(0,9) for i in range(4)]
    return HttpResponse("本期号码： "+ str(lottery_num)+ "           " +localtime)
    #return HttpResponse(localtime)

# Create your views here.
'''