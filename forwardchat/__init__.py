import discord
from typing import Final

from redbot.core import commands
from redbot.core.bot import Red


class ForwardChat(commands.Cog):
    CHANNEL_ID: Final[int] = 1564822502297833603  

    def __init__(self, bot: Red):
        self.bot = bot

    @commands.command()
    async def sendtrivia(self, ctx: commands.Context, *, text: str):
        """Send a message to the staff channel."""
        channel = self.bot.get_channel(self.CHANNEL_ID)
        await channel.send(
            f"**{ctx.author}**: {text}",
            allowed_mentions=discord.AllowedMentions.none(),
        )
        await ctx.author.send(f"Your message has been sent:\n> {text}")
        await ctx.message.delete()


async def setup(bot: Red):
    await bot.add_cog(ForwardChat(bot))
