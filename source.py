import os
import discord

client = discord.Client()

@client.event
async def on_ready():
    print("The bot is ready!")
    client.change_presence(game=discord.Game(name="Hellow world"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "Hello":
        await client.send_message(message.channel, "World")

TOKEN = os.getenv("NzI0MDAyODMzMTQ5NDYwNTkx.Xu58Aw.Guk_uwMxOFC5oqcqnzdNoAQcAnU")
