import discord
import random
from discord.ext import commands
import giphy_client
from giphy_client.rest import ApiException

giphy_token = 'y6UOLOhiDjQc3hk65cJRVyv3A3mKYFHy'
api_instance = giphy_client.DefaultApi()

class Giphy(commands.Cog):

    def __init__(self, client):
        self.client = client

    async def search_gifs(self ,query):
        try:
            response = api_instance.gifs_search_get(giphy_token, query, limit=100, rating='g')
            lst = list(response.data)
            gif = random.choices(lst)

            return gif[0].url

        except ApiException as e:
            return "Exception when calling DefaultApi->gifs_search_get: %s\n" % e

    @commands.command(name='gif')
    async def gifmeme(self, ctx):
        gif = await search_gifs('meme')
        await ctx.send(gif)

def setup(client):
    client.add_cog(Giphy(client))