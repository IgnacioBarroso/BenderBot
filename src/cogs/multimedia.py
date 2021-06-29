from w2g import w2g
import clipboard
import discord
from discord.ext import commands
from discord.ext.commands.core import command
from urllib import parse, request
import re

class Multimedia(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def youtube(self, ctx, *, search):
        query_string = parse.urlencode({'search_query': search})
        html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
        search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
        await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

    @commands.command()
    async def w2gw(self, ctx, search):
        w2g.w2g(search)
        await ctx.send(clipboard.paste())

def setup(client):
    client.add_cog(Multimedia(client))