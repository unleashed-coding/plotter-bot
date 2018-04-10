#!/usr/bin/env python3

import os
from os import path

import sympy as syp
from discord.ext.commands import Bot


bot = Bot(command_prefix='p$')
TOKEN = os.environ.get('TOKEN')

if not path.exists('.log'): os.mkdir('.log')
log_dir = path.abspath('.log')


@bot.event
async def on_ready():
    me = f'{bot.user.name}#{bot.user.discriminator} <@{bot.user.id}>'
    print(f'Logged in as {me}')
    print('Bot ready!')


@bot.command(aliases=['test'])
async def hello(*args):
    return await bot.say('Hello world!')


@bot.command(pass_context=True)
async def plot(ctx, *, exp):
    exp = syp.sympify(exp)

    img_path = path.join(log_dir, 'figure.png')
    img = syp.plot(exp, show=False)
    img.save(img_path)

    return await bot.upload(img_path)


bot.run(TOKEN) if TOKEN else print('TOKEN environment variable not set!')
