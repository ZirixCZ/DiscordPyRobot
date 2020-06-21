import os
import discord

#this is our secret token ok, dont loose it
TOKEN = "NzI0MDAyODMzMTQ5NDYwNTkx.Xu58Aw.Guk_uwMxOFC5oqcqnzdNoAQcAnU"
client = discord.Client()

#this will tell us if the bot connected to the server (respektive jestli máme správný token omegalulw)
@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(activity=discord.Game("yo wuddap"))


@client.event
async def on_message(message): #this will take the on_message function from discord lib and make it into def so we can use it mweeeeew

    if message.author == client.user: #this will check if the sender is someone else than the acctual client (nebude odpovídat na své zprávy - zamezí se loopům)
        return
    if message.content == "Hello":
        await message.channel.send("world") #line 20 až 21 je simple send message command

client.run(TOKEN) #připojí se na token přes discord api
