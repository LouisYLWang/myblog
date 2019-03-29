# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Airbnb_tools
from .forms import raw_urlForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
import json
import re



# Create your views here.

def index(request):
    if request.method == 'POST':

        form = raw_urlForm(request.POST)
        if form.is_valid():
            url = form['fields']
            context = {'url': url}
            return render(request, 'blog/airbnb_tool_result.html',context=context)

    if request.method == 'GET': 
        return render(request, 'blog/airbnb_tool_index.html')


def result(request):#, url):

    #house =  get_object_or_404(Airbnb_tools, url = raw_url)
    #
    return render(request, 'blog/airbnb_tool_result.html')#, context=context)

def get_rooms_by_Host(room_url):

	room_id = re.findall( '[0-9]{5,10}',room_url)[0]
	#url = "https://www.airbnb.cn/api/v2/pdp_listing_details/13770112?_format=for_rooms_show&adults=1&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&"
	response = requests.get(url)
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
	r1 = requests.get(url, headers=headers)
	d=r1.json()
	host_id = d['pdp_listing_detail']['user']['id']
	room_listing_url = 'https://www.airbnb.cn/api/v2/user_promo_listings?_limit=50&_offset=0&currency=CNY&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=zh&user_id=%s' %host_id
	r2 = requests.get(room_listing_url, headers=headers)
	room_json = r2.json()
	room_id_listing = [i['id'] for i in room_json['user_promo_listings']]
	return room_id_listing


