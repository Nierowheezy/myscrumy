import json
from boto3 import client
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ChatMessage, Connection


ENDPOINT_URL = 'https://4hvqalbj8k.execute-api.us-east-2.amazonaws.com/test'


def _parse_body(body):
    body_unicode = body.decode('utf-8')
    return json.loads(body_unicode)


def _send_to_connection(connection_id, data):
    gatewayapi = client('apigatewaymanagementapi',
                        endpoint_url="https://4hvqalbj8k.execute-api.us-east-2.amazonaws.com/test",
                        region_name='us-east-2',
                        aws_access_key_id='AKIAIXJ3QVQOFRF5DWKA',
                        aws_secret_access_key='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')
    Data = json.dumps(data).encode('utf-8')
    return gatewayapi.post_to_connection(ConnectionId=connection_id, Data=Data)


# Create your views here.
@csrf_exempt
def test(request):
    return JsonResponse({'message': 'Hello Daud'}, status=200)


@csrf_exempt
def connect(request):
    body = _parse_body(request.body)
    print(body)
    connection_id = body['connectionId']
    print(connection_id)
    Connection.objects.create(connection_id=connection_id)
    return JsonResponse({"message": "connected successfully"}, status=200)


@csrf_exempt
def disconnect(request):
    body = _parse_body(request.body)
    print(body)
    connection_id = body['connectionId']
    print(connection_id)
    Connection.objects.create(connection_id=connection_id)
    Connection.delete()
    return JsonResponse({"message": 'disconnected successfully'}, status=200)


@csrf_exempt
def send_message(request):
    body = _parse_body(request.body)
    print(body)
    client = Connection.objects.get(connection_id=body['connectionId'])
    ChatMessage.objects.create(
        username=body['username'],
        message=body['message'],
        timestamp=body['timestamp'],
        client=client
    )
    connections = [_.connection_id for _ in Connection.objects.all()]
    data = {'messages': [body]}
    for connection in connections:
        _send_to_connection(connection, data)

    return JsonResponse({"message": "successfully sent"}, status=200)


@csrf_exempt
def get_recent_messages(request):
    body = _parse_body(request.body)
    connection_id = body['connectionId']
    messages = []
    for message in ChatMessage.objects.all():
        messages.append(
            {
                'username': message.username,
                'message': message.message,
                'timestamp': message.timestamp
            }
        )
   data = {'messages': messages}
   _send_to_connection(connection_id, data)

   return JsonResponse({'message': 'success'}, status=200)
