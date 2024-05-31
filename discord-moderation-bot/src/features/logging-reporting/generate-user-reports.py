import discord
from discord.ext import commands

class GenerateUserReports(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('User Reports Module is ready.')

    @commands.command(name='generate_report')
    async def generate_report(self, ctx, user: discord.User):
        # Logic to generate user report
        await ctx.send(f'Generating report for user: {user.name}')

def setup(bot):
    bot.add_cog(GenerateUserReports(bot))