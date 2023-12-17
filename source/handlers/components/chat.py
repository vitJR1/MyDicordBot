import typing

from random import randrange

from bot import bot


@bot.command()
async def flip(ctx):
    await ctx.send(f"{ctx.message.author.mention}, {randrange(2) == 0}")


@bot.command()
async def roll(ctx, n: typing.Optional[int] = 0, m: typing.Optional[int] = 0):
    await ctx.send(f"{ctx.message.author.mention}, {randrange(min(n, m), max(n, m)) if m != n else randrange(0, 100)}")
