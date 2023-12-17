from discord.ext import commands

from intent import intents

bot = commands.Bot(command_prefix='/', intents=intents)

bot.remove_command('help')
