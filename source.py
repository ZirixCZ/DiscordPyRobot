import os
import asyncio
import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = 'getme ')
token = "NzI0MDAyODMzMTQ5NDYwNTkx.Xu58Aw.Guk_uwMxOFC5oqcqnzdNoAQcAnU" #this is our secret token ok, dont loose it

async def status_task():
    while True:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="getme help"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game("Created by:"))
        await asyncio.sleep(2)
        await client.change_presence(activity=discord.Game("Péro, Zirix, SNICKERS"))
        await asyncio.sleep(3)

@client.event
async def on_ready():
    print("The bot is ready!")
    await client.loop.create_task(status_task())


for filename in os.listdir(r'python\discord\membot\cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token) #připojí se na token přes discord api
