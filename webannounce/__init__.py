import datetime
from typing import Final, Optional, cast

import discord
from discord.ext import tasks
from redbot.core.bot import Red
from redbot.core import commands


class WebAnnounce(commands.Cog):
    GUILD_ID: Final[int] = 374032112426156042
    CHANNEL_ID: Final[int] = 806658072503517244
    WEBHOOK_ID: Final[int] = 806863336763424779
    
    def __init__(self, bot: Red) -> None:
        self.bot: Red = bot

    @staticmethod
    def is_message_recent(message: discord.Message, minutes: int = 60) -> bool:
        now: datetime.datetime = datetime.datetime.now(datetime.timezone.utc)
        time_difference: datetime.timedelta = now - message.created_at
        minutes_difference: float = time_difference.total_seconds() / 60
        return minutes_difference <= minutes

    @staticmethod
    async def get_last_message(channel: discord.TextChannel) -> discord.Message:
        message: discord.Message = await channel.fetch_message(
            channel.last_message_id
        )
        return message
    
    async def cog_load(self) -> None:
        self.check_for_webhook_updates.start()
        return await super().cog_load()
        
    async def cog_unload(self) -> None:
        self.check_for_webhook_updates.cancel()
        return await super().cog_unload()

    @tasks.loop(seconds=60)
    async def check_for_webhook_updates(self):
        guild: Optional[discord.Guild] = self.bot.get_guild(self.GUILD_ID)
        if not guild:
            raise
        if (
            not len(guild.members) / getattr(guild, "member_count", 0) > 0.9
            and self.bot.intents.members
        ):
            await guild.chunk(cache=True)
        channel: discord.TextChannel = cast(
            discord.TextChannel, guild.get_channel(self.CHANNEL_ID)
        )
        try:
            message: discord.Message = await self.get_last_message(channel)
        except discord.NotFound:
            return
        if not message.webhook_id:
            return
        if message.webhook_id != self.WEBHOOK_ID:
            return
        if not self.is_message_recent(message):
            await message.channel.send(f"There hasn't been any messages in 60 minutes <@234515446659940353>")
async def setup(bot):
    await bot.add_cog(WebAnnounce(bot))