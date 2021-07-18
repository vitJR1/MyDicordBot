import discord
from discord.ext import commands
import fun
import asyncio
import time

bot = commands.Bot(command_prefix=(".", "!", ">"))
bot.remove_command('help')

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
async def mute(ctx,member:discord.Member,time:int, *args):
	reason = ""
	for i in args:
		reason += i + " "
	channel = bot.get_channel(864505851498725376)
	muterole = discord.utils.get(ctx.guild.roles, id = 864506206077059113)
	emb = discord.Embed(title = "Mute", color = 0xff0000)
	emb.add_field(name = "Модератор", value = ctx.message.author.mention, inline=False)
	emb.add_field(name = "Нарушитель", value = member.mention, inline=False)
	emb.add_field(name = "Причина", value = reason, inline=False)
	emb.add_field(name = "Время", value = time, inline=False)
	await member.add_roles(muterole)
	await channel.send(embed = emb)
	await asyncio.sleep(time*60)
	await member.remove_roles(muterole)

@bot.command()
@commands.has_permissions(view_audit_log=True)
async def unmute(ctx,member:discord.Member):
	channel = bot.get_channel(864505851498725376)
	muterole = discord.utils.get(ctx.guild.roles, id = 864506206077059113)
	emb = discord.Embed(title = "Unmute", color = 0xff0000)
	emb.add_field(name = "Модератор", value = ctx.message.author.mention, inline=False)
	emb.add_field(name = "Нарушитель", value = member.mention, inline=False)
	await channel.send(embed = emb)
	await member.remove_roles(muterole)

@bot.command()
async def bb(ctx):
	try:
		channel = ctx.message.author.voice.channel	
		await ctx.send("You are connected to "+str(channel))
	except:
		await ctx.send("You are not connected to a voice channel")
	fun.mess("bb")

@bot.event
async def on_ready():
	fun.createbd()
	global time_dict
	time_dict = {}
	print('Logged on as {0}!'.format(bot.user))
	await bot.change_presence(status=discord.Status.online, activity=discord.Game("Quests creator"))

@bot.event
async def on_message(message):
	await bot.process_commands(message)	
	if message.author != bot.user:
		print('Message from {0.author}: {0.content}'.format(message))
		if fun.checkmessage(message.content):
			await message.channel.send('Общайтесь культурней))')
		fun.newritesql(message.author,0,True)
		rank_upped = fun.uprank(message.author)
		if rank_upped[0]:
			await message.channel.send('{0}, вы были повышены до ранга {1}!'.format(message.author.mention,rank_upped[1]))
@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        time_dict[member] = time.time()
    elif before.channel is not None and after.channel is None:
        t2 = time.time() - time_dict[member]
        del time_dict[member]
        fun.newritesql(member, round(t2/60), False)

bot.run("NzAzNzYxMjk5MDExNjY1OTY4.XqTSyA.ISClhc1opwQD2-dZPtIhKhOMt1M")
