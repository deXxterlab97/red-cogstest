import datetime
from typing import Final, Optional, cast

import discord
from discord.ext import tasks
from redbot.core.bot import Red
from redbot.core import commands

FILE=/owlcityfact.txt

class owlcityfact(commands.Cog):
    CHANNEL_ID: Final[int] = 1030666245361631242
    @tasks.loop(minutes=3)
    async def post_random_line():
        with open(FILE, encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(random.choice(lines))

async def setup(bot):
    await bot.add_cog(owlcityfact())
