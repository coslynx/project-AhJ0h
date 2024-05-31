import discord
from discord.ext import commands, tasks
import datetime

class Reminders(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reminders = {}

    @tasks.loop(seconds=60)
    async def check_reminders(self):
        now = datetime.datetime.now()
        for user_id, reminders in self.reminders.items():
            for reminder in reminders:
                if now > reminder['datetime']:
                    user = self.bot.get_user(user_id)
                    await user.send(f"Reminder: {reminder['message']}")
                    reminders.remove(reminder)

    @commands.command(name='setreminder')
    async def set_reminder(self, ctx, time, *, message):
        try:
            time = int(time)
            reminder_time = datetime.datetime.now() + datetime.timedelta(minutes=time)
            if ctx.author.id not in self.reminders:
                self.reminders[ctx.author.id] = []
            self.reminders[ctx.author.id].append({'datetime': reminder_time, 'message': message})
            await ctx.send(f"Reminder set for {time} minutes from now.")
        except ValueError:
            await ctx.send("Invalid time format. Please enter a valid number of minutes.")

def setup(bot):
    bot.add_cog(Reminders(bot))