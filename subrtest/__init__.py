import praw
import random
import discord
from discord.ext import commands
from redbot.core.bot import Red
from redbot.core import commands

reddit = praw.Reddit(client_id='p4UNCgfF0qQW9XhglMJo5Q',
                     client_secret='YRJM-PB3nQwK7vPauxfbVIw8xf92zQ',
                     user_agent='babu97')

class subrtest(commands.Cog):
    @commands.command()    
    async def sub1(self, ctx, arg):
        
        sub = reddit.subreddit('arg').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in sub if not x.stickied)
        await ctx.send(submission.url)

async def setup(bot):
    await bot.add_cog(subrtest())