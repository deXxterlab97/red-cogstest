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
       if filepath == 'events':
            now = datetime.now()
            month = now.strftime("%B")
            await ctx.send(f'**Releases for current month of {month}:**')
            month = month.lower()
            with open(path + month + ".txt", "r") as fp:
                await ctx.send(fp.read())
       else:
            month = filepath.capitalize()
            await ctx.send (f'**Releases for the month of {month}:**')
            with open(path + filepath + ".txt", "r") as fp:
                await ctx.send(fp.read())
                
            
            

async def setup(bot):
    await bot.add_cog(occalendar())
            