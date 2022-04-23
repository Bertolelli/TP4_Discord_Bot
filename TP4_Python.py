# from lib2to3.pgen2 import tokenize
# from typing import Optional
# import asyncio

import discord
from discord.ext import commands
import logging

token = 'OTU4Njg3MDc0NTQ5MTA4ODA3.YkQ86g.LV6CFQ_Xj6POHg_HzMNA2q8O7Lo'

bot = commands.Bot(command_prefix = ".")

@bot.event
async def on_ready():
    print('test')
        

@bot.command(aliases = ['Hello', 'Hi', 'Bonjour', 'bonjour', 'hello', 'yo', 'h'])
async def hi(ctx):
    await ctx.send("Hello there")


@commands.has_permissions(administrator=True)
@bot.command(aliases=['p'])
async def clean(ctx, amount=5):
    await ctx.channel.purge(limit=amount + 1)


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


bot.run(token)