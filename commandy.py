import discord
import random
from discord.ext import commands

class Commandy(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def hello(self, ctx):
        await ctx.send('world')

    @commands.command(aliases=["GH"])
    async def GitHub(self, ctx):
        await ctx.send('https://github.com/ZirixCZ/DiscordPyRobot')

    @commands.command()
    async def meme(self, ctx):
        memes = ["69","420","https://imgur.com/a/C6sONwG"] #memes pro random choice
        await ctx.send(random.choice(memes))


def setup(client):
    client.add_cog(Commandy(client))

