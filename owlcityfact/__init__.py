import random
from pathlib import Path
from typing import Final, List

from discord.ext import tasks
from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.data_manager import cog_data_path

FILE = Path(__file__).parent / "owlcityfact.txt"


class OwlCityFact(commands.Cog):
    CHANNEL_ID: Final[int] = 1030660521172676668

    def __init__(self, bot: Red):
        self.bot = bot
        self.queue_file = cog_data_path(self) / "owlcityfact_queue.txt"
        self.last_sent: str | None = None

    async def cog_load(self):
        self.post_random_line.start()

    async def cog_unload(self):
        self.post_random_line.cancel()

    @staticmethod
    def _read_lines(path: Path) -> List[str]:
        if not path.exists():
            return []
        with open(path, encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]

    def _write_queue(self, lines: List[str]) -> None:
        with open(self.queue_file, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

    def _make_shuffled_copy(self) -> List[str]:
        lines = self._read_lines(FILE)
        random.shuffle(lines)
        if len(lines) > 1 and lines[0] == self.last_sent:
            lines[0], lines[-1] = lines[-1], lines[0]
        self._write_queue(lines)
        return lines

    @tasks.loop(hours=10)
    async def post_random_line(self):
        queue = self._read_lines(self.queue_file)
        if not queue:
            queue = self._make_shuffled_copy()
            if not queue:
                return  # Original file is empty

        channel = self.bot.get_channel(self.CHANNEL_ID)
        if channel is None:
            return  # Channel not available; keep the queue as is

        line = queue[0]
        ran = random.randint(1, 100)
        await channel.send(f"Owl City random fact #{ran}: {line}")

        self.last_sent = line
        self._write_queue(queue[1:])

    @post_random_line.before_loop
    async def before_post(self):
        await self.bot.wait_until_red_ready()


async def setup(bot: Red):
    await bot.add_cog(OwlCityFact(bot))
