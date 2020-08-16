import os
import discord
from discord.ext import commands
import random
import giphy_client
from giphy_client.rest import ApiException
from pprint import pprint

client = commands.Bot(command_prefix = 'getme ')
token = 'NzI0MDAyODMzMTQ5NDYwNTkx.Xu52Lg.XTg1VTGMaetmydQ4_UEr1yTW0pY'

@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(activity=discord.Game("yo wuddap"))


for filename in os.listdir(r'python\discord\membot\cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#this is our secret token ok, dont loose it
client.run(token)
