from main import bot
from source import fun


@bot.command()
async def help(ctx):
    await ctx.send(fun.help())
    fun.mess("help")


@bot.command()
async def flip(ctx):
    await ctx.send(fun.flip())
    fun.mess("flip")


@bot.command()
async def roll(ctx, *args):
    await ctx.send(fun.roll(args))
    fun.mess("roll")


@bot.command()
async def top(ctx):
    await ctx.send(fun.topmessages())
    fun.mess("top")


@bot.command()
async def me(ctx):
    await ctx.send(fun.me(ctx.message.author))
    fun.mess("me")


@bot.command()
async def prediction(ctx):
    await ctx.send(fun.prediction())
    fun.mess("prediction")


@bot.command()
@commands.has_permissions(view_audit_log=True)
async def mute(ctx, member: discord.Member, time: int, *args):
    reason = ""
    for i in args:
        reason += i + " "
    channel = bot.get_channel(864505851498725376)
    muterole = discord.utils.get(ctx.guild.roles, id=864506206077059113)
    emb = discord.Embed(title="Mute", color=0xff0000)
    emb.add_field(name="Модератор", value=ctx.message.author.mention, inline=False)
    emb.add_field(name="Нарушитель", value=member.mention, inline=False)
    emb.add_field(name="Причина", value=reason, inline=False)
    emb.add_field(name="Время", value=time, inline=False)
    await member.add_roles(muterole)
    await channel.send(embed=emb)
    await asyncio.sleep(time * 60)
    await member.remove_roles(muterole)


@bot.command()
@commands.has_permissions(view_audit_log=True)
async def unmute(ctx, member: discord.Member):
    channel = bot.get_channel(864505851498725376)
    muterole = discord.utils.get(ctx.guild.roles, id=864506206077059113)
    emb = discord.Embed(title="Unmute", color=0xff0000)
    emb.add_field(name="Модератор", value=ctx.message.author.mention, inline=False)
    emb.add_field(name="Нарушитель", value=member.mention, inline=False)
    await channel.send(embed=emb)
    await member.remove_roles(muterole)


@bot.command()
async def bb(ctx):
    try:
        channel = ctx.message.author.voice.channel
        await ctx.send("You are connected to " + str(channel))
    except:
        await ctx.send("You are not connected to a voice channel")
    fun.mess("bb")
