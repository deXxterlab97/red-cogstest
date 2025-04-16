import copy
import random

import discord
from discord.ext import tasks
from redbot.core.bot import Red
from redbot.core import commands

file = open('/home/dex/DiscordQuotes.csv', 'r+')

MESSAGE = file.read()

MESSAGE = MESSAGE.splitlines()

class RandomMess(commands.Cog):
    @commands.command()
    async def randommess(self, ctx):
        global message1
        message = str(random.choice(MESSAGE))
        message1 = message.split(",")
        msg = message1[0]
        await ctx.send(msg)
    @commands.command()
    async def randomans(self, ctx):
        msg2 = message1[1]
        await ctx.send(msg2)

async def setup(bot):
    await bot.add_cog(RandomMess())
