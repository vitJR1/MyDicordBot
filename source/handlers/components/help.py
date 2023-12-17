from bot import bot


@bot.command()
async def help(ctx):
    await ctx.send("""
    flip - подбросить монетку
    roll - рандомное число от 0 до 100
    top - топ 10 участников по сообщениям
    me - вся информация о тебе
    help - а это я, команда - помощник))
    """)

