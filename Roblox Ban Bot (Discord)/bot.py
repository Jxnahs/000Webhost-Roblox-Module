# Game ban and Game unban command. Only the people with certain roles can use this command but you can always change this. EG: @commands.has_any_role('Owner')


import requests
import discord
from discord.ext import commands


Webhost = "" # Your 000webhost url


ApiUrl = "https://api.roblox.com/"


bot = commands.Bot(command_prefix=';',help_command=None) # Change the prefix here

@bot.event
async def on_ready():
    print("--- Bot is online! --- ")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Jonah's thing")) # Change activity here


@bot.command()
@commands.has_any_role('Creators', 'Data Manager') # You can change role names
async def gameban(ctx, username=None):
    if username == None:
        await ctx.send("Please provide the persons username!")
    else:
        await ctx.send(f"Banning {username}!")
        getid = requests.get(f"{ApiUrl}users/get-by-username?username={username}")
        try:
            id = getid.json()['Id']
            r = requests.get(f'{Webhost}update.php?database=Bans&key={id}&value=true')
            await ctx.send(f"Banned {username}/{id}")
        except:
            await ctx.send("That username is invalid")

@gameban.error
async def gameban_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        em = discord.Embed(description=f"You need the Owner or Data Manager role to use this command!", color=ctx.author.color)
        await ctx.send(ctx.author.mention, embed=em)
    else:
        raise error  


@bot.command()
@commands.has_any_role('Creators', 'Data Manager') # You can change role names
async def gameunban(ctx, username=None):
    if username == None:
        await ctx.send("Please provide the persons username!")
    else:
        await ctx.send(f"Unbanning {username}!")
        getid = requests.get(f"{ApiUrl}users/get-by-username?username={username}")
        try:
            id = getid.json()['Id']
            r = requests.get(f'{Webhost}/update.php?database=Bans&key={id}&value=false')
            await ctx.send(f"Unbanned {username}/{id}")
        except:
            await ctx.send("That username is invalid")
        


@gameunban.error
async def gameunban_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        em = discord.Embed(description=f"You need the Owner or Data Manager role to use this command!", color=ctx.author.color)
        await ctx.send(ctx.author.mention, embed=em)
    else:
        raise error






bot.run("token") # Get your bot token here 
