import copy
import random

import discord
from discord.ext import tasks
from redbot.core.bot import Red
from redbot.core import commands

file = open('/home/dex/output101.txt', 'r+')

MESSAGE = file.read()

MESSAGE = MESSAGE.splitlines()

class RandomMess(commands.Cog):
    @commands.command()
    async def randommess(self, ctx):
        message = str(random.choice(MESSAGE))
        await ctx.send(message)
    

async def setup(bot):
    await bot.add_cog(RandomMess())
