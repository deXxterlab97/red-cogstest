import discord
import math
from discord.ext import tasks
from redbot.core.bot import Red
from redbot.core import commands

class relic(commands.cog):
    @commands.command()
    async def relictime(self, ctx, r1, r2, r3):
               
        r1_no_ref = (120+45)/16*1.37
        r2_no_ref = (120+45)/16*0.93
        r3_no_ref = (120+45)/16*0.66
        
        r1_1_ref = (240+45)/16*1.37
        r2_1_ref = (240+45)/16*0.93
        r3_1_ref = (240+45)/16*0.66
        
        r1_2_ref = (360+45)/16*1.37
        r2_2_ref = (360+45)/16*0.93
        r3_2_ref = (360+45)/16*0.66
        
        r1_3_ref = (480+45)/16*1.37
        r2_3_ref = (480+45)/16*0.93
        r3_3_ref = (480+45)/16*0.66
        
        time_r1_no_ref = math.ceil(r1/r1_no_ref)
        time_r2_no_ref = math.ceil(r2/r2_no_ref)
        time_r3_no_ref = math.ceil(r3/r3_no_ref)
        
        await ctx.send(f"White relic no refresh: {time_r1_no_ref} day(s)")


async def setup(bot):
    await bot.add_cog(relic())        