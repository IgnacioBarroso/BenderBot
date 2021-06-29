import discord
import datetime
from discord import client
from discord.ext import commands
from discord.ext.commands.core import command

class ServerInfo(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')
    
    @commands.command()
    async def clear_5(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)
    
    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(title= f"{ctx.guild.name}", description='Lorem impsum',
        timestamp= datetime.datetime.utcnow(), color=discord.Colour.blue())
        embed.add_field(name="Server creado el", value=f"{ctx.guild.created_at}")
        embed.add_field(name="Creador", value=f"{ctx.guild.owner}")
        embed.add_field(name="Region", value=f"{ctx.guild.region}")
        embed.add_field(name="ID", value=f"{ctx.guild.id}")
        embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(ServerInfo(client))