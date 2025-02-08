import discord
from discord.ext import commands
from redbot.core import commands

class MembersList(commands.Cog):
    
    @commands.command()
    async def memberid(self, ctx:commands.Context):
        """List all User ID of a server
        """
        
        msg = ""
        guild = ctx.guild
        members = [member for member in guild.members if not member.bot]
        for member in members:
            membersid=str(member.id)
            msg+= " " + membersid
        await ctx.send(msg)    
                
async def setup(bot):
    await bot.add_cog(MembersList())