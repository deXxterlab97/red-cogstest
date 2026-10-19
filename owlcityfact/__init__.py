import random
from pathlib import Path
from typing import Final

from discord.ext import tasks
from redbot.core import commands
from redbot.core.bot import Red

FILE = Path(__file__).parent / "owlcityfact.txt"


class OwlCityFact(commands.Cog):
    CHANNEL_ID: Final[int] = 1030660521172676668

    def __init__(self, bot: Red):
        self.bot = bot
    async def cog_load(self):
        self.post_random_line.start()
    async def cog_unload(self):
        self.post_random_line.cancel()

    @tasks.loop(hours=6)
    async def post_random_line(self):
        with open(FILE, encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
        channel = self.bot.get_channel(self.CHANNEL_ID)
        ran = random.randint (1,100)
        await channel.send(f"Owl City random fact #{ran}: {random.choice(lines)}")

    @post_random_line.before_loop
    async def before_post(self):
        await self.bot.wait_until_red_ready()


async def setup(bot: Red):
    await bot.add_cog(OwlCityFact(bot))
