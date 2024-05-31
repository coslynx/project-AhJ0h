import discord

class MultiServerSupport:
    def __init__(self, client):
        self.client = client

    async def on_ready(self):
        print('Multi-Server Support is ready.')

    async def on_message(self, message):
        if message.author == self.client.user:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Hello!')

client = discord.Client()
multi_server_support = MultiServerSupport(client)

@client.event
async def on_ready():
    await multi_server_support.on_ready()

@client.event
async def on_message(message):
    await multi_server_support.on_message(message)

client.run('your_token_here')