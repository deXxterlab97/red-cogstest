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
        
        total_no_ref = time_r1_no_ref + time_r2_no_ref + time_r3_no_ref
        
        time_r1_1_ref = math.ceil(float(r1)/float(r1_1_ref))
        time_r2_1_ref = math.ceil(float(r2)/float(r2_1_ref))
        time_r3_1_ref = math.ceil(float(r3)/float(r3_1_ref))
        
        total_1_ref = time_r1_1_ref + time_r2_1_ref + time_r3_1_ref
        
        time_r1_2_ref = math.ceil(float(r1)/float(r1_2_ref))
        time_r2_2_ref = math.ceil(float(r2)/float(r2_2_ref))
        time_r3_2_ref = math.ceil(float(r3)/float(r3_2_ref))
        
        total_2_ref = time_r1_2_ref + time_r2_2_ref + time_r3_2_ref
        
        time_r1_3_ref = math.ceil(float(r1)/float(r1_3_ref))
        time_r2_3_ref = math.ceil(float(r2)/float(r2_3_ref))
        time_r3_3_ref = math.ceil(float(r3)/float(r3_3_ref))
        
        total_3_ref = time_r1_3_ref + time_r2_3_ref + time_r3_3_ref
        
        
        
        await ctx.send(f"White relic no refresh: {time_r1_no_ref} day(s)\nGreen relic no refresh: {time_r2_no_ref} day(s)\nBlue relic no refresh: {time_r3_no_ref} day(s)\nTotal: {total_no_ref} day(s)")
        await ctx.send(f"White relic with 1 refresh: {time_r1_1_ref} day(s)\nGreen relic with 1 refresh: {time_r2_1_ref} day(s)\nBlue relic with 1 refresh: {time_r3_1_ref} day(s)\nTotal: {total_1_ref} day(s)")
        await ctx.send(f"White relic with 2 refreshes: {time_r1_2_ref} day(s)\nGreen relic with 2 refreshes: {time_r2_2_ref} day(s)\nBlue relic with 2 refreshes: {time_r3_2_ref} day(s)\nTotal: {total_2_ref} day(s)")
        await ctx.send(f"White relic with 3 refreshes: {time_r1_3_ref} day(s)\nGreen relic with 3 refreshes: {time_r2_3_ref} day(s)\nBlue relic with 3 refreshes: {time_r3_3_ref} day(s)\nTotal: {total_3_ref} day(s)")
    @commands.command()
    async def relics(self, ctx, r3, r4, r5, r6, r7, r8, r9):
        white_sd = r3*35+r4*55+r5*75+r6*95+r7*115+r8*135+r9*165
        green_sd = r3*15+r4*40+r5*65+r6*90+r7*115+r8*140+r9*170
        blue_sd = r5*15+r6*40+r7*75+r8*120+r9*175
        
        await ctx.send(f"White relic needed: {white_sd}\nGreen relic needed: {green_sd}\nBlue relic needed: {blue_sd}")
    @commands.command()
    async def shard (self, ctx, starcount, shardcount, cantina_cost, hard):
        day = 0
        if hard == 1:
            await ctx.send("Hard is 1")
            if starcount == 3:
                day = (65+85+100+30-shardcount)/5
            elif starcount == 4:
                day = (65+85+100-shardcount)/5
            elif starcount == 5:
                day = (85+100-shardcount)/5
            elif starcount == 6:
                day = (100-shardcount)/5
            else:
                await ctx.send("Something is wrong")
            await ctx.send(f"Time to take a hard node character to 7 stars: {math.ceil(day)}")
        else:
            await ctx.send("Hard isn't 1")
            cantina_daily = math.ceil((120 + 360 + 45) / float(cantina_cost))
            await ctx.send(f"Cantina daily: {cantina_daily}")
            if starcount == 3:
                day = (65+85+100+30-shardcount)/cantina_daily
            elif starcount == 4:
                day = (65+85+100-shardcount)/cantina_daily
            elif starcount == 5:
                day = (85+100-shardcount)/cantina_daily
            elif starcount == 6:
                day = (100-shardcount)/cantina_daily
            else:
                await ctx.send("Something is wrong")
            day = math.ceil(day)    
            await ctx.send(f"Time to take a cantina node character to 7 stars: {day}")
                    
async def setup(bot):
    await bot.add_cog(relic())        