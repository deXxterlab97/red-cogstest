import discord
import asyncio
from redbot.core import commands

class Countdown(commands.Cog):
    @commands.command()
    async def counter(self, ctx, time: int):
        """Countdown to the time specified in seconds, in intervals of 5 seconds.
        """
        timer = time
        if timer>0 and timer < 21600:
            message = await ctx.send(f"{timer}s left.")
            while (timer):
                await asyncio.sleep(5)
                timer -= 5
                if timer>0:
                    await message.edit(content=f"{timer}s left.")
                else:
                    await message.edit(content=f"Time's up, {ctx.author.mention}! {time}s has passed.")
        else:
            message = await ctx.send(f"Can't do negatives and more than 6 hours!")
                

async def setup(bot):
    await bot.add_cog(Countdown())
        
