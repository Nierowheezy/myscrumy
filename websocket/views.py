import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
import boto3
# Create your views here.


def _parse_body(body):
    body_unicode = body.decode('utf-8')
    print(body_unicode)
    return json.loads(body)


@csrf_exempt
def test(request):
    return JsonResponse({'message': 'hello Daud'}, status=200)


@csrf_exempt
def connect(request):
    body = _parse_body(request.body)
    print(body)
    connection_id = body['connectionId']
    print(connection_id)
    id = CreateConnection.objects.create(connection_id=connection_id)
    id.save()
    return JsonResponse({"message": "connected successfuly"}, status=200)


@csrf_exempt
def disconnect(request):
    body = _parse_body(request.body)
    print(body)
    connection_id = body['connectionId']
    print(connection_id)
    id = CreateConnection.objects.get(connection_id=connection_id)
    id.delete()
    return JsonResponse("disconnected successfuly", status=200, safe=False)


def _send_to_connection(connection_id, data):
    gatewayapi = boto3.client(
        'apigatewaymanagementapi',
        endpoint_url='https://mjnzsaiqld.execute-api.us-east-1.amazonaws.com/test',
        region_name='us-east-1',
        aws_access_key_id='AKIAIUEH5GZT4HVAJVJQ',
        aws_secret_access_key='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'
    )
    return gatewayapi.post_to_connection(
        ConnectionId=connection_id,
        Data=json.dumps(data).encode('utf-8'))


@csrf_exempt
def send_message(request):
    body = _parse_body(request.body)
    chat = ChatMessage()
    chat.username = body['username']
    chat.message = body['message']
    chat.timestamp = body['timestamp']
    chat.save()
    connections = CreateConnection.objects.all()
    data = {'messages': [body]}
    for connection in connections:
        _send_to_connection(connection.connection_id, data)
    return JsonResponse({"message": "successfully sent"}, status=200)
