import datetime
from typing import Final, Optional, cast

import discord
from discord.ext import tasks
from redbot.core.bot import Red
from redbot.core import commands


class occalendar(commands.Cog):
    """Calendar of important Owl City events."""
    @commands.command()
    async def ocreleases(self, ctx, arg):
        """Lists important events"""    
        
        f = open ('owlcityevents.csv', 'r+')
        await ctx.send(f)
        
        if arg == 'january':
            f2 = open('test2.txt', 'r+')
            await ctx.send(f2)
            
        month = datetime.now().month

async def setup(bot):
    await bot.add_cog(occalendar())
            