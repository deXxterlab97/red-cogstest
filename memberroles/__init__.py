import discord
from discord.ext import tasks
from redbot.core.bot import Red
from redbot.core import commands
from discord.ext import commands

class memberroles(commands.Cog):
    @commands.command()
    async def memberroles(self, ctx):
        role = ctx.guild.get_role(1533590480170778654)
        members = [
            member.display_name
            for member in ctx.guild.members
            if role not in member.roles
        ]
        await ctx.send("\n".join(members))

async def setup(bot):
    await bot.add_cog(memberroles())  
    


