import discord
from discord.ext import commands
import os
import random

intenst = discord.Intents.default()
intenst.message_content = True

bot = commands.Bot(command_prefix='$', intents=intenst)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def mem(ctx):
    lst = os.listdir('images')
    with open(f'images/{random.choice(lst)}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
            picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def animals(ctx):
    lst = os.listdir('ima')
    with open(f'ima/{random.choice(lst)}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
            picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

bot.run('MTI0OTAwMDkzMTQ5NzA4NzAwNg.G9Ct1m.45xxI-Frk-sWtQK3ruh4OX4JcrutPQmtHCgQFo')