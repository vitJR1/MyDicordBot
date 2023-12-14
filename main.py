import discord
from discord.ext import commands
from source import fun
import time
import os

bot = commands.Bot(command_prefix=('/', '>'))
bot.remove_command('help')

bot.run(os.getenv('DISCORD_TOKEN'))
