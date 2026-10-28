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
        # Working copy lives in Red's data folder, so the original is never touched
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
        lines = self._read_lines(FILE)  # Original is read only
        random.shuffle(lines)
        # Avoid repeating the same fact back-to-back across a reshuffle
        if len(lines) > 1 and lines[0] == self.last_sent:
            lines[0], lines[-1] = lines[-1], lines[0]
        self._write_queue(lines)
        return lines

    @tasks.loop(hours=6)

async def setup(bot):
    await bot.add_cog(OwlCityFact(bot))
