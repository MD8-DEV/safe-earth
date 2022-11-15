from channels.generic.websocket import AsyncWebsocketConsumer
from user_auth.models import *
from channels.db import SyncToAsync
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_room_name = self.scope['url_route']['kwargs']['room']
        await self.channel_layer.group_add(
            self.group_room_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.group_room_name,
            self.channel_name
        )
        return code
    
    async def receive(self, text_data):
        loaded_data = json.loads(text_data)
        await self.channel_layer.group_send(
            self.group_room_name,
            {
                "type":"chat_message",
                "user":loaded_data["user"],
                "text":loaded_data["text"]
            }
        )
        await self.store_msg(loaded_data["text"], loaded_data["user"])
        return None
    
    async def chat_message(self, data):
        await self.send(json.dumps({
            "data":data["text"],
            "user":data["user"]
        }))

    @SyncToAsync
    def store_msg(self, msg, user):
        Message.objects.create(
            text=msg,
            room=Room.objects.get(name=self.group_room_name),
            user=User.objects.get(username=user)
        )
