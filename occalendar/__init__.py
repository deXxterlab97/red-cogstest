from datetime import datetime

import discord
from redbot.core.bot import Red
from redbot.core import commands


class occalendar(commands.Cog):
    """Calendar of important Owl City events."""
    @commands.command()
    async def ocreleases(self, ctx, filepath="events"):
       path = '/home/dex/babu97/cogs/CogManager/cogs/occalendar/'
       filepath = filepath.lower()
       if filepath == 'current':
            now = datetime.now()
            month = now.strftime("%B").lower()
            with open(path + month + ".txt", "rb") as fp:
                await ctx.send(fp.read())
       else:
            with open(path + filepath + ".txt", "rb") as fp:
                await ctx.send(fp.read())
                
            
            

async def setup(bot):
    await bot.add_cog(occalendar())
            