import discord
import random
import datetime
from time import gmtime, strftime
from redbot.core import commands
from redbot.core.utils.chat_formatting import pagify


class Penis(commands.Cog):
    """Penis related commands."""

    @commands.command()
    async def penis(self, ctx, *users: discord.Member):
        """Detects user's penis length

        This is 100% accurate.
        Enter multiple users for an accurate comparison!"""
        if not users:
            await ctx.send_help()
            return

        dongs = {}
        msg = ""
        
        time = strftime("%-H",gmtime())
        fulltime = strftime("%I%p",gmtime())
        
        for user in users:
            time2 = int(time) + int(user.id)
            
            random.seed(time2)
            
            if ctx.bot.user.id == user.id:
                length = 50
            else:
                length = random.randint(0, 30)

            dongs[user] = "8{}D".format("=" * length)

        
        dongs = sorted(dongs.items(), key=lambda x: x[1])

        for user, dong in dongs:
            msg += "**{}'s size at {}:**\n{}\n".format(user.display_name, fulltime, dong)

        for page in pagify(msg):
            await ctx.send(page)
        
