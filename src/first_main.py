import clipboard
import test
import datetime
import re
from urllib import parse, request
from asyncio.locks import Event
import discord
from discord.ext import commands
from discord.ext.commands import bot
from discord.ext.commands.bot import Bot

bot = commands.Bot(command_prefix='>', description='Soy el bot de juancito')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)

@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@bot.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unnbaned {user.mention}')
            return

@bot.command()
async def clear_5(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@bot.command()
async def helpy(ctx):
    await ctx.send('''COMMANDS:
    All commands init with '>'
    >youtube :Search:  | for first link of a search
    >w2g :YouTubeLink: | for view Youtube sync with friends
    >ping              | for pong
    >info              | for server info
    >sum :num1: :num2: | for add two numbers
    >helpy             | for help 
    ''')

@bot.command()
async def w2g(ctx, search):
    test.test_w2g(search)
    await ctx.send(clipboard.paste())

@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title= f"{ctx.guild.name}", description='Lorem impsum',
    timestamp= datetime.datetime.utcnow(), color=discord.Colour.blue())
    embed.add_field(name="Server creado el", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Creador", value=f"{ctx.guild.owner}")
    embed.add_field(name="Region", value=f"{ctx.guild.region}")
    embed.add_field(name="ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")
    await ctx.send(embed=embed)

@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name='Bender', url='http://www.twitch.tv/accountname'))
    print('Ready')

bot.run('')