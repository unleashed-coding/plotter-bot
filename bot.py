#!/usr/bin/env python3

import os

from discord.ext.commands import Bot


bot = Bot(command_prefix="plot ")
TOKEN = os.environ.get("TOKEN")


@bot.event
async def on_ready():
    me = f'{bot.user.name}#{bot.user.discriminator} <@{bot.user.id}>'
    print(f'Logged in as {me}')
    print('Bot ready!')


@bot.command(aliases=['test'])
async def hello(*args):
    return await bot.say('Hello world!')


bot.run(TOKEN) if TOKEN else print('TOKEN environment variable not set!')
