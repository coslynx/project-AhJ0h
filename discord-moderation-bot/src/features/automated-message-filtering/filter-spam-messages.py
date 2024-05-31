file: discord-moderation-bot/src/features/automated-message-filtering/filter-spam-messages.py

import discord

class SpamMessageFilter:
    def __init__(self, client):
        self.client = client

    async def filter_spam_messages(self, message):
        if len(message.content) > 100:
            await message.delete()
            await message.channel.send(f"{message.author.mention}, please refrain from sending spam messages.")
        else:
            await message.channel.send("Message is not considered as spam.")

def setup(client):
    client.add_cog(SpamMessageFilter(client))