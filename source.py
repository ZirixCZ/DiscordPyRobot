import os
import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = '.')

#this will tell us if the bot connected to the server (respektive jestli máme správný token omegalulw)
@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(activity=discord.Game("yo wuddap"))

@client.command()
async def hello(ctx):
    await ctx.send('world')

@client.command(aliases=["GH"])
async def GitHub(ctx):
    await ctx.send('https://github.com/ZirixCZ/DiscordPyRobot')

@client.command()
async def meme(ctx):
    memes = ["69","420","https://imgur.com/a/C6sONwG"] #memes pro random choice
    await ctx.send(random.choice(memes))

#this is our secret token ok, dont loose it
client.run("NzI0MDAyODMzMTQ5NDYwNTkx.Xu58Aw.Guk_uwMxOFC5oqcqnzdNoAQcAnU") #připojí se na token přes discord api

