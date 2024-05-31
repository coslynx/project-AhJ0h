import discord
from discord.ext import commands

class BotResponsesCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hello', help='Responds with a hello message')
    async def hello(self, ctx):
        await ctx.send('Hello! How can I assist you today?')

    @commands.command(name='goodbye', help='Responds with a goodbye message')
    async def goodbye(self, ctx):
        await ctx.send('Goodbye! Have a great day!')

    @commands.command(name='thanks', help='Responds with a thank you message')
    async def thanks(self, ctx):
        await ctx.send('You\'re welcome! Feel free to ask if you need any help.')

    @commands.command(name='info', help='Provides information about the bot')
    async def info(self, ctx):
        embed = discord.Embed(title='Discord Moderation Bot', description='A bot to help manage servers efficiently', color=discord.Color.blue())
        embed.add_field(name='Features', value='Automated Message Filtering, User Management, Customizable Commands, Logging and Reporting, Scheduled Tasks', inline=False)
        embed.set_footer(text='For more information, visit our website')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(BotResponsesCommands(bot))