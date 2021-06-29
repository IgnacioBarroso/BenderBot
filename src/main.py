import discord
import os
from discord.activity import CustomActivity
from discord.ext import commands

client = commands.Bot(command_prefix='>')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    
@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./src/cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='l esclavo'))
    print('I\'m ready')
    
client.run('ODU4NTgxNjI3ODE0MDE5MDgy.YNgOcw.t3z2e9SUREfsoFKw69jLl75SvxA')