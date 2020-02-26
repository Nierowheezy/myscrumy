from django.contrib import admin
from websocket.models import Connection, ChatMessage
# Register your models here.
admin.site.register(Connection)
admin.site.register(ChatMessage)
