import discord
from discord.ext import commands

class LogModerationActions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('Invalid command used.')

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        channel = discord.utils.get(message.guild.text_channels, name='mod-logs')
        if channel:
            await channel.send(f'Message deleted: {message.content}')

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        channel = discord.utils.get(guild.text_channels, name='mod-logs')
        if channel:
            await channel.send(f'{user.name} has been banned.')

    @commands.Cog.listener()
    async def on_member_unban(self, guild, user):
        channel = discord.utils.get(guild.text_channels, name='mod-logs')
        if channel:
            await channel.send(f'{user.name} has been unbanned.')

def setup(bot):
    bot.add_cog(LogModerationActions(bot))