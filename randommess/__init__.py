import copy
import random

from redbot.core import commands

file = open('/home/dex/output101.csv', 'r+')

MESSAGE = file.read()

MESSAGE = MESSAGE.strip().split()

class RandomMess(commands.Cog):
    @commands.command()
    async def randommess(self, ctx):
        await message.channel.send(MESSAGE)
    

async def setup(bot):
    await bot.add_cog(RandomMess())
