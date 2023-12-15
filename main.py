from os import getenv

from discord import Client
from discord.ext import commands

client = Client()
bot = commands.Bot(command_prefix=('/', '>'))
bot.remove_command('help')

bot.run(getenv('DISCORD_TOKEN'))
