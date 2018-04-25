# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.template import loader
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
#from .models import Item
import json
from StringIO import StringIO
from collections import defaultdict
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal
import boto3
from boto3.dynamodb.conditions import Key, Attr
#from login.forms import *


@csrf_exempt
def main(request):
    try:
	id_1 = request.POST.get('itid', 'N/A')
	dynamodb = boto3.resource('dynamodb',
                          	aws_access_key_id='AKIAJH7QCO7VUC43PFYQ',
                                aws_secret_access_key='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'
                              , region_name='us-east-2')
        table = dynamodb.Table(name=u'ItemTracker_tbl')
        response = table.get_item(Key = {'itemtrackerId':id_1})
        #list1 = []
        context = {'lat':response['Item']['lat'],'lon':response['Item']['lon']}
        #with open('details.json','w') as det:
        #        json.dump(list1,det)
        template = loader.get_template('polls/main.html')
        return HttpResponse(template.render(context,request))
    except:
        ad = []
	context = {'ad':ad}
	template = loader.get_template('polls/error.html')
        return HttpResponse(template.render(context,request))

def req():
        client = boto3.resource(
        'dynamodb',
        aws_access_key_id='',
        aws_secret_access_key='',
        )
        return client

@csrf_exempt
def test(request):
        itid = request.POST.get('itid',"N/A")
        itid = str(itid)
        client = req()
        table = client.Table('latlon')
        response = table.get_item(
                Key={
                'ItemId':itid
                }
        )
        context={'response':response}
        template=loader.get_template('polls/test.html')
        return HttpResponse(template.render(context,request))

def index(request):
        ad=[]
        context={'ad':ad}
        template=loader.get_template('polls/index.html')
        return HttpResponse(template.render(context,request))

def receiver(request):
        data_write=defaultdict(lambda:{})
        if request.method=="POST":
                Id=request.POST.get('Id',"N/A")
                latitude=request.POST.get('latitude',"N/A")
                longitude=request.POST.get('longitude',"N/A")
                with open('details.json','r') as det:
                        data=json.load(det)
                        data_write=data
                        if Id in data_write.keys():
                                data_write[Id]["latitude"].append(latitude)
                                data_write[Id]["longitude"].append(longitude)
                        else:
                                data_write[Id]={}
                                data_write[Id]["latitude"]=[]
                                data_write[Id]["longitude"]=[]
                                data_write[Id]["latitude"].append(latitude)
                                data_write[Id]["longitude"].append(longitude)
                        data_write=data
                with open('details.json','w') as details_write:
                        json.dump(data_write,details_write)
                context ={'ad'}
        template=loader.get_template('polls/results.html')
        
        return HttpResponse(template.render(context,request))
