import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Add logic here to detect and delete inappropriate content
    if "bad_word" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention}, please refrain from using inappropriate language.")

bot.run('YOUR_TOKEN')