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

@client.command(aliases=["Hello"])
async def hello(ctx):
    await ctx.send('world')

@client.command(aliases=["GH", "gh", "github", "Github", "Gh"])
async def GitHub(ctx):
    await ctx.send('https://github.com/ZirixCZ/DiscordPyRobot')

@client.command(aliases=["Meme", "mm"])
async def meme(ctx):
    memes = ["69","420","https://imgur.com/a/C6sONwG"] #memes pro random choice
    await ctx.send(random.choice(memes))

@client.command(aliases=["Getmehelp", "gmh", "Gmh"]) #help prikaz keby chceli vidiet commandy
async def GetMeHelp(ctx):
    await ctx.send("`Github = ukáže link na GitHub repository\n meme = náhodny meme`")

#this is our secret token ok, dont loose it
client.run("NzI0MDAyODMzMTQ5NDYwNTkx.XvJxIg.4HqXv_UrDykJzPF-8NY0WNt_KC0") #připojí se na token přes discord api
