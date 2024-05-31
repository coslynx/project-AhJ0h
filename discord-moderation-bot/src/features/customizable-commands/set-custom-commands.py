import discord

class CustomCommands:
    def __init__(self, client):
        self.client = client

    async def set_custom_commands(self, message):
        if message.content.startswith('!add'):
            command = message.content.split(' ')[1]
            response = ' '.join(message.content.split(' ')[2:])
            # Add custom command to a database or file
            await message.channel.send(f'Custom command "{command}" has been added with response "{response}".')

    async def on_message(self, message):
        if message.author == self.client.user:
            return

        await self.set_custom_commands(message)

def setup(client):
    client.add_cog(CustomCommands(client))