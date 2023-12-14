from main import bot
from source import fun


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
        fun.newritesql(message.author, 0, True)
        rank_upped = fun.uprank(message.author)
        if rank_upped[0]:
            await message.channel.send(
                '{0}, вы были повышены до ранга {1}!'.format(message.author.mention, rank_upped[1]))


@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        time_dict[member] = time.time()
    elif before.channel is not None and after.channel is None:
        t2 = time.time() - time_dict[member]
        del time_dict[member]
        fun.newritesql(member, round(t2 / 60), False)
