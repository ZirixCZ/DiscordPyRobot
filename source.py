import os
import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = 'getme ')

@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(activity=discord.Game("yo wuddap"))


for filename in os.listdir(r'discord\membot\cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#this is our secret token ok, dont loose it
client.run("NzI0MDAyODMzMTQ5NDYwNTkx.Xu58Aw.Guk_uwMxOFC5oqcqnzdNoAQcAnU") #připojí se na token přes discord api
