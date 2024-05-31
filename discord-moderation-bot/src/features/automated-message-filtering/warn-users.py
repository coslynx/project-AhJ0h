import discord


class WarnUsersCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        # Detect inappropriate content
        if "inappropriate_word" in message.content:
            await message.channel.send(f"{message.author.mention}, please refrain from using inappropriate language.")
            # Warn user for violating rules
            await message.author.send("You have violated the server rules by using inappropriate language.")

    @commands.command(name='warn')
    async def warn_user(self, ctx, member: discord.Member):
        # Warn user for misconduct
        await ctx.send(f"{member.mention}, you have been warned for misconduct.")
        await member.send("You have received a warning for misconduct in the server.")


def setup(bot):
    bot.add_cog(WarnUsersCog(bot))