import os
import discord
from discord.ext import commands
import random

client = discord.Client()

#this will tell us if the bot connected to the server (respektive jestli máme správný token omegalulw)
@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(activity=discord.Game("yo wuddap"))
    memes = ["69","420"] #memes pro random choice

@client.event
async def on_message(message): #this will take the on_message function from discord lib and make it into def so we can use it mweeeeew

    if message.author == client.user: #this will check if the sender is someone else than the acctual client (nebude odpovídat na své zprávy - zamezí se loopům)
        return
    if message.content == "Hello":
        await message.channel.send("world") #line 20 až 21 je simple send message command
    elif message.content == "GitHub":
        await message.channel.send("https://github.com/ZirixCZ/DiscordPyRobot")
    elif message.content == "meme":
        await message.channel.send(random.choice(memes))

#this is our secret token ok, dont loose it
client.run("NzI0MDAyODMzMTQ5NDYwNTkx.Xu58Aw.Guk_uwMxOFC5oqcqnzdNoAQcAnU") #připojí se na token přes discord api
