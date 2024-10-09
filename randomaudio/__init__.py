import copy
import random

from redbot.core import commands

file = open('/home/dex/musictest/songs.txt', 'r+')

TRACKS = file.read()

TRACKS = TRACKS.strip().split()

class RandomAudio(commands.Cog):
    @commands.command()
    async def playrandom(self, ctx):
        global track
        track = random.choice(TRACKS)
        msg = copy.copy(ctx.message)
        msg.content = ctx.prefix + "play " + track
        ctx.bot.dispatch("message", msg)
    @commands.command()
    async def playrepeat(self, ctx):
        msg = copy.copy(ctx.message)
        msg.content = ctx.prefix + "play " + track
        ctx.bot.dispatch("message", msg)

async def setup(bot):
    await bot.add_cog(RandomAudio())
