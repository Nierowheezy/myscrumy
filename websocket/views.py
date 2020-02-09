import json
from .models import ChatMessage, Connection
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import boto3
# Create your views here.
@csrf_exempt
def test(request):
    return JsonResponse({'message': 'Hello Daud'}, status=200)


def _parse_body(body):
    body_unicode = body.decode('utf-8')
    return json.loads(body_unicode)


@csrf_exempt
def connect(request):
    body = _parse_body(request.body)
    connection_id = body['connectionId']
    Connection.objects.create(connection_id=connection_id)
    response = {
        "statusCode": 200,
        "body": "Connect succesfully"
    }
    # return response
    return JsonResponse('connect successfully', status=200, safe=False)


@csrf_exempt
def disconnect(request):
    body = _parse_body(request.body)
    connection_id = body['connectionId']
    Connection.objects.get(connection_id=connection_id).delete()
    return JsonResponse('disconnect successfully', status=200, safe=False)


def _send_to_connection(connection_id, data):
    gatewayapi = boto3.client('apigatewaymanagementapi',
                              endpoint_url=" https://4hvqalbj8k.execute-api.us-east-2.amazonaws.com/test/@connections",
                              region_name='us-west-2',
                              aws_access_key_id='AKIAIUEH5GZT4HVAJVJQ',
                              aws_secret_access_key='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')
    return gatewayapi.post_to_connection(ConnectionId=connection_id, Data=json.dumps(data).encode('utf-8'))


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


@csrf_exempt
def get_recent_messages(request):
    body = _parse_body(request.body)
    connections = ChatMessage.objects.all()
    return JsonResponse({'messages': [{'username': connection.username, 'message': connection.message,
                                       'timestamp': connection.timestamp} for connection in connections]}, status=200)
