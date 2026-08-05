import discord
from discord.ext import tasks
from redbot.core.bot import Red
from redbot.core import commands

class memberroles(commands.Cog):
    @commands.command()
    async def memberroles(ctx):
        for member in ctx.message.server.members:
            if not get(member.roles, name='Verified Owl'):
                await ctx.send(member)
    
async def setup(bot):
    await bot.add_cog(memberroles())            
            
    


