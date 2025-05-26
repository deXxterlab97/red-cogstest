import datetime
from typing import Final, Optional, cast

import discord
from discord.ext import tasks
from redbot.core.bot import Red
from redbot.core import commands


class occalendar(commands.Cog):
    """Calendar of important Owl City events."""
    @commands.command()
    async def ocreleases(self, ctx, filepath: "releases"):
        if filepath == 'current':
            now = datetime.now()
            month = now.strftime("%B")
            with open(month + ".txt", "r") as fp:
                await ctx.send(f.read())
        else:        
            with open(filepath + ".txt", "r") as fp:
                await ctx.send(f.read())
            
            

async def setup(bot):
    await bot.add_cog(occalendar())
            