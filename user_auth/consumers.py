from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            "UL_Groupe",
            self.channel_name
        )
        self.accept()
    
    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            "UL_group",
            self.channel_name
        )
    
