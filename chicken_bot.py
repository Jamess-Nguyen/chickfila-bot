import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

class Client(discord.Client):
    async def on_ready(self):
        print("chickenbot online")
        
        channel = self.get_channel(CHANNEL_ID)
        if channel:
            await channel.send("hello world") 
        await self.close() 

intents = discord.Intents.default()
intents.message_content = True
client = Client(intents=intents)
client.run(TOKEN)
