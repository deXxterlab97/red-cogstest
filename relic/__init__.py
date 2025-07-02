import discord
import math
from discord.ext import tasks
from redbot.core.bot import Red
from redbot.core import commands

class relic(commands.Cog):
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
        
        time_r1_no_ref = math.ceil(float(r1)/float(r1_no_ref))
        time_r2_no_ref = math.ceil(float(r2)/float(r2_no_ref))
        time_r3_no_ref = math.ceil(float(r3)/float(r3_no_ref))
        
        total_no_ref = time_r1_no_ref + time_r2_no_ref + time_r2_no_ref
        
        time_r1_1_ref = math.ceil(float(r1)/float(r1_1_ref))
        time_r2_1_ref = math.ceil(float(r2)/float(r2_1_ref))
        time_r3_1_ref = math.ceil(float(r3)/float(r3_1_ref))
        
        total_1_ref = time_r1_1_ref + time_r2_1_ref + time_r2_1_ref
        
        time_r1_2_ref = math.ceil(float(r1)/float(r1_2_ref))
        time_r2_2_ref = math.ceil(float(r2)/float(r2_2_ref))
        time_r3_2_ref = math.ceil(float(r3)/float(r3_2_ref))
        
        total_2_ref = time_r1_2_ref + time_r2_2_ref + time_r3_2_ref
        
        time_r1_3_ref = math.ceil(float(r1)/float(r1_3_ref))
        time_r2_3_ref = math.ceil(float(r2)/float(r2_3_ref))
        time_r3_3_ref = math.ceil(float(r3)/float(r3_3_ref))
        
        total_3_ref = time_r1_3_ref + time_r2_3_ref + time_r3_3_ref
        
        
        
        await ctx.send(f"White relic no refresh: {time_r1_no_ref} day(s)\nGreen relic no refresh: {time_r2_no_ref} day(s)\nBlue relic no refresh: {time_r3_no_ref} day(s)\nTotal: {total_no_ref}")
        await ctx.send(f"White relic with 1 refresh: {time_r1_1_ref} day(s)\nGreen relic with 1 refresh: {time_r2_1_ref} day(s)\nBlue relic with 1 refresh: {time_r3_1_ref} day(s)\nTotal: {total_1_ref}")
        await ctx.send(f"White relic with 2 refreshes: {time_r1_2_ref} day(s)\nGreen relic with 2 refreshes: {time_r2_2_ref} day(s)\nBlue relic with 2 refreshes: {time_r3_2_ref} day(s)\nTotal: {total_2_ref}")
        await ctx.send(f"White relic with 3 refreshes: {time_r1_3_ref} day(s)\nGreen relic with 3 refreshes: {time_r2_3_ref} day(s)\nBlue relic with 3 refreshes: {time_r3_3_ref} day(s)\nTotal: {total_3_ref}")


async def setup(bot):
    await bot.add_cog(relic())        