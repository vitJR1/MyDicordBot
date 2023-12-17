import env.include

from os import getenv
from source.bot import *
from source.handlers.components.help import *
from source.handlers.components.chat import *


bot.run(getenv('DISCORD_TOKEN'))
