import json
import boto3
from .models import ChatMessage, Connection
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from itertools import chain

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
        "body": "Connecte succesfully"
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
                              endpoint_url="https://4hvqalbj8k.execute-api.us-east-2.amazonaws.com/test/",
                              region_name='us-east-2',
                              aws_access_key_id='',
                              aws_secret_access_key='')
    return gatewayapi.post_to_connection(ConnectionId=connection_id, Data=json.dumps(data).encode('utf-8'))


def to_dict(instance):
    opts = instance._meta
    data = {}
    for f in chain(opts.concrete_fields, opts.private_fields):
        data[f.name] = f.value_from_object(instance)
    for f in opts.many_to_many:
        data[f.name] = [i.id for i in f.value_from_object(instance)]
    return data


@csrf_exempt
def send_message(request):
    body = _parse_body(request.body)
    print(body)
    instance = ChatMessage()
    print(body['body']['content'])
    instance.content = body['body']['content']
    instance.username = body['body']['username']
    instance.timestamp = body['body']['timestamp']
    instance.save()
    connections = Connection.objects.all()
    data = {"messages": [body]}
    print("{} - {}".format(connections, data))
    for connection in connections:
        _send_to_connection(connection.connection_id, data)

    return JsonResponse({'message': 'successfully send'}, status=200)

# getting 5 recent messages
@csrf_exempt
def get_recent_messages(request):
    instances = ChatMessage.objects.all()
    body = _parse_body(request.body)
    print(body)
    connection_id = body['connectionId']
    print("{} - {}".format('heeehoo', connection_id))
    messages = []
    for instance in instances:
        messages.append(to_dict(instance))
    print(messages)
    data = {'message': messages}
    _send_to_connection(connection_id, data)
    return JsonResponse({'message': 'fetch successful'}, status=200)
