import csv
import io
import random
from typing import Final

import aiohttp
from discord.ext import tasks
from redbot.core import commands
from redbot.core.bot import Red

SHEET_ID = "Y18AxXNGlxQ5HEVYMZuLjII1rXLgpk9IEIOKkJVdW3doE"
SHEET_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv&gid=0"


class OwlCityFact(commands.Cog):
    CHANNEL_ID: Final[int] = 1030666245361631242

    def __init__(self, bot: Red):
        self.bot = bot
        self.session = aiohttp.ClientSession()

    async def cog_load(self):
        self.post_random_line.start()

    async def cog_unload(self):
        self.post_random_line.cancel()
        await self.session.close()

    @tasks.loop(minutes=3)
    async def post_random_line(self):
        async with self.session.get(SHEET_URL) as resp:
            text = await resp.text()
        rows = csv.reader(io.StringIO(text))
        lines = [row[0].strip() for row in rows if row and row[0].strip()]
        channel = self.bot.get_channel(self.CHANNEL_ID)
        ran = random.randomint(1,100)
        await channel.send(f"Random Owl City Fact #{ran}: {random.choice(lines)}")

    @post_random_line.before_loop
    async def before_post(self):
        await self.bot.wait_until_red_ready()


async def setup(bot: Red):
    await bot.add_cog(OwlCityFact(bot))
