import datetime
from typing import Final, Optional, cast

import discord
from discord.ext import tasks
from redbot.core.bot import Red
from redbot.core import commands


class occalendar(commands.Cog):
    """Calendar of important Owl City events."""
    @commands.command()
    async def ocreleases(self, ctx, filepath: "text"):
        with open(filepath + ".txt", "r") as fp:
            await ctx.send(f.read())
            
            month = datetime.now().month

async def setup(bot):
    await bot.add_cog(occalendar())
            