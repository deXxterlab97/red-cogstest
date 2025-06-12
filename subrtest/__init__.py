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
        
        sub = reddit.subreddit(arg).hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in sub if not x.stickied)
            e = discord.Embed(title=f'Requested by {ctx.author}', description=f'{submission.title}')
            e.set_image(url=submission.url)
        await ctx.send(embed=e)
        await ctx.send(f'{reddit.config.reddit_url} + {submission.permalink}')

async def setup(bot):
    await bot.add_cog(subrtest())