import praw
import random
import discord
from discord.ext import commands
from redbot.core.bot import Red
from redbot.core import commands

reddit = praw.Reddit(client_id='p4UNCgfF0qQW9XhglMJo5Q',
                     client_secret='YRJM-PB3nQwK7vPauxfbVIw8xf92zQ',
                     user_agent='discord')

class subrtest(commands.Cog):    
    async def sub1():
        memes_submissions = reddit.subreddit('boobs').hot()
        post_to_pick = random.randint(1, 10)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

        await bot.say(submission.url)

async def setup(bot):
    await bot.add_cog(subrtest())