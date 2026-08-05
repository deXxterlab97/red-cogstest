import discord
from discord.ext import tasks
from redbot.core.bot import Red
from redbot.core import commands

class memberroles(commands.Cog):
    @commands.command()
    async def memberroles(self, ctx, role: discord.Role):
        await ctx.send("**Start processing**")  
        for member in ctx.guild.members:
            if not member.bot and role not in member.roles:
                await ctx.send(member.display_name)
        await ctx.send("**Finish processing**")            
async def setup(bot):
    await bot.add_cog(memberroles())
