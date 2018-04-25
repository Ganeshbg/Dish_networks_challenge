#!/usr/bin/python
# -*- coding: utf-8 -*-
from suds.client import Client
import geocoder
import time
i=0
while(i<10):
    time.sleep(10)
    g = geocoder.ip('me')
    c = Client('http://localhost:8030/?wsdl')
    c.service.say_hello('Macbookair', str(g.latlng[0])+','+str(g.latlng[1]))
    i = i+1


##import boto3
##from boto3.dynamodb.conditions import Key, Attr
##dynamodb = boto3.resource('dynamodb',
##                          aws_access_key_id='AKIAIGEWAQQRTVXDW3ZA   aws_secret_access_key='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'
##                          ,region_name='us-east-2')
##dynamodb_client = boto3.client('dynamodb', aws_access_key_id = 'AKIAIGEWAQQRTVXDW3ZA',
##                        aws_secret_access_key = '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',
##                        region_name = 'us-east-2')
##
##table = dynamodb.Table(name=u'ItemTracker_tbl')
##response  = table.query(KeyConditionExpression=Key('itemtrackerId').eq("ABC123"))
##print(response)
##

##
##import boto3
##from boto3.dynamodb.conditions import Key, Attr
##dynamodb = boto3.resource('dynamodb', aws_access_key_id = 'AKIAI7HHEQFZZ6KQ536A',
##                        aws_secret_access_key = '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',
##                        region_name = 'us-east-2')
##dynamodb_client = boto3.client('dynamodb', aws_access_key_id = 'AKIAI7HHEQFZZ6KQ536A',
##                        aws_secret_access_key = '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',
##                        region_name = 'us-east-2')
##
##existing_tables = dynamodb_client.list_tables()['TableNames']
##print(existing_tables)
##table_name = 'ItemTracker_tbl'
##itemtrackerId = 'ABC123'
##if table_name not in existing_tables:
##    table = dynamodb.create_table(TableName=table_name,
##                                  KeySchema=[{'AttributeName': 'itemtrackerId'
##                                              , 'KeyType': 'HASH'}],
##                                  AttributeDefinitions=[{'AttributeName': 'itemtrackerId'
##                                                         , 'AttributeType': 'S'}],
##                                  ProvisionedThroughput={'ReadCapacityUnits': 5,
##                                                         'WriteCapacityUnits': 5})
##
##    # Wait until the table exists.
##    table.meta.client.get_waiter('table_exists').wait(TableName='ItemTracker_tbl')
##
##table = dynamodb.Table('ItemTracker_tbl')
##
##table.put_item(Item = { 'itemtrackerId':itemtrackerId,'lat' : ['12.23'], 'lon':['11.23'] })
##table.update_item(Key={'itemtrackerId': itemtrackerId},
##                              UpdateExpression='SET lat = list_append(lat, :i)'
##                              , ExpressionAttributeValues={':i': ['12.3']},
##                              ReturnValues='UPDATED_NEW')
##response  = table.query(KeyConditionExpression=Key('itemtrackerId').eq('123')
##)
##
##
