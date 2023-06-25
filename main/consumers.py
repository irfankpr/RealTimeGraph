from  channels.generic.websocket import AsyncWebsocketConsumer
import json
from  random import randint
from asyncio import sleep



class WSconsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()
        for i in range(100):
            await self.send(json.dumps( {"message": randint(1,30)} ))
            await sleep(1)