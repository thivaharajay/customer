from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import boto3
import json
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError


def index(request):
    template = loader.get_template('files.html')

    dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-2',
                              aws_access_key_id='AKIAJJFIBS77IMSXRW4A',
                              aws_secret_access_key='Pd/dLcc+9kxZCYSejnQEaKhrRay5zQygdqdtKph')
    table = dynamodb.Table("22175666")

    items = []
    try:
        response = table.scan()
        data = json.dumps(response['Items'])
        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            data.extend(response['Items'])

    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        context = {'items': response['Items']}

        return HttpResponse(template.render(context, request))