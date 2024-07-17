import discord
import os

TOKEN = 'urtoken'
CHANNEL_ID = urchannelid

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Connecté en tant que {self.user}')
        channel = self.get_channel(CHANNEL_ID)
        if channel is not None:
            await channel.send('@everyone Le serveur est prêt !')
        else:
            print(f'Le canal avec l\'ID {CHANNEL_ID} n\'a pas été trouvé.')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)
