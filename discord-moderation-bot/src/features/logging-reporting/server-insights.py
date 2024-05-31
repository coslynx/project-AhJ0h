import discord
from discord.ext import commands
import matplotlib.pyplot as plt

class ServerInsights(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Server Insights cog is ready')

    @commands.command(name='generate_report')
    async def generate_report(self, ctx):
        # Logic to generate and send server insights report
        server = ctx.guild
        members = server.members
        member_count = len(members)

        # Generate a bar chart of member count
        plt.bar('Total Members', member_count)
        plt.xlabel('Server Insights')
        plt.ylabel('Member Count')
        plt.title('Server Member Insights')
        plt.savefig('member_insights.png')

        # Send the generated report
        await ctx.send(file=discord.File('member_insights.png'))

def setup(bot):
    bot.add_cog(ServerInsights(bot))