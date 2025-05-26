from datetime import datetime

import discord
from redbot.core.bot import Red
from redbot.core import commands


class occalendar(commands.Cog):
    """Calendar of important Owl City events."""
    @commands.command()
    async def ocreleases(self, ctx, filepath="events"):
       
        with open(filepath + ".txt", "r") as fp:
             await ctx.send(f.read())
            
            

async def setup(bot):
    await bot.add_cog(occalendar())
            