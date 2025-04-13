from .webannounce import webannounce

async def setup(bot):
  await bot.add_cog(webannounce())