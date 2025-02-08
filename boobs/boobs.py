import discord
import random
import datetime
from time import gmtime, strftime
from redbot.core import commands
from redbot.core.utils.chat_formatting import pagify


class Boobs(commands.Cog):
    """Boobies related commands."""

    @commands.command()
    async def boobscompare(self, ctx, *users: discord.Member):
        """Detects user's breast size

        This is 110% accurate and have been tested on males and females.
        Enter multiple users for an accurate comparison!"""
        if not users:
            await ctx.send_help()
            return

        boobs = {}
        msg = ""
        state = random.getstate()
        time = strftime("%-H",gmtime())
        fulltime = strftime("%I %p",gmtime())
        for user in users:
            random.seed(str(time))

            if ctx.bot.user.id == user.id:
                length = 50
            else:
                length = random.randint(0, 20)

            boobs[user] = "({}•{})({}•{})".format(" " * length," " * length," " * length," " * length)

        random.setstate(state)
        boobs = sorted(boobs.items(), key=lambda x: x[1])

        for user, boob in boobs:
            msg += "**{}'s size at {} (GMT time):**\n{}\n".format(user.display_name, fulltime, boob)

        for page in pagify(msg):
            await ctx.send(page)
            
