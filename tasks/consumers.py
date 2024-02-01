from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
import json
from .models import Notification, Task
from channels.db import database_sync_to_async


class NofificationConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        user = self.scope['user']
        if user.is_authenticated:
            self.group_name = user.username
            await self.channel_layer.group_add(self.group_name, self.channel_name) 
            await self.send({
                'type': 'websocket.accept',
            })

    # async def websocket_receive(self, event):
    #     # print("Websocket message received.......", event)
    #     user = self.scope['user']
    #     if user.is_authenticated:
            
    #         await self.channel_layer.group_send(self.group_name, {  # send message to group
    #             'type': 'send.notification', # own event, we can write any thing but we need to create handler for this event
    #             'message': event['text'],
    #         })

    async def send_notification(self, event): # event: chat.message and handler will be chat_message replace "." by "_"
        '''Here sent message to client from server'''
        # print("Event ....", event) 
        print('Send Notification....')
        await self.send({
            'type': 'websocket.send',
            'text': json.dumps({'msg':event['message'], 'task':event['task']}) # convert dict to string
        })

        
    async def websocket_disconnect(self, event):
        user = self.scope['user']
        if user.is_authenticated:
            await self.channel_layer.group_discard(self.group_name, self.channel_name) # discard this channel from this group
        raise StopConsumer()
 