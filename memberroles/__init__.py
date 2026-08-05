import discord
from discord.ext import tasks
from redbot.core.bot import Red
from redbot.core import commands

class memberroles(commands.Cog):
    @commands.command()
    async def memberroles(self, ctx, roleid):
        role = ctx.guild.get_role(roleid)
        members = [
            member.display_name
            for member in ctx.guild.members
            if role not in member.roles
        ]
        for member in members:
            await ctx.send(member)
async def setup(bot):
    await bot.add_cog(memberroles())
