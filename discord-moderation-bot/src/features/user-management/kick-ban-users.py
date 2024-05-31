# kick-ban-users.py

import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message):
    if message.content.startswith('!kick'):
        member = message.mentions[0]
        await member.kick(reason='Kicked by moderation bot')
        await message.channel.send(f'{member.name} has been kicked.')

    if message.content.startswith('!ban'):
        member = message.mentions[0]
        await member.ban(reason='Banned by moderation bot')
        await message.channel.send(f'{member.name} has been banned.')

client.run('your_token_here')