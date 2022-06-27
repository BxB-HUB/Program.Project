from cgitb import text
from sqlite3 import Timestamp
from turtle import title
from click import pass_context
import discord
import pastebin
import requests
import datetime
import time
from time import sleep
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure
from datetime import datetime
import sys
import json
from json import loads, load
from discord.gateway import DiscordWebSocket  #, _log
from discord.ext.commands import Bot
from discord_webhook import DiscordWebhook, DiscordEmbed
with open('setting.json') as f:
    config = json.load(f)
token = config.get('Token')
prefix = config.get('prefix')
api1 = config.get('pastebin_cookie')
api = pastebin.login(api1)
bot = commands.Bot(command_prefix=prefix, help_command=None)
intents = discord.Intents.default()
intents.members = True


pastebincode = ""

@bot.command()
@has_permissions(administrator=True)
async def addhwid(ctx, hwid):
    await ctx.message.delete()
    old = requests.get(f"https://pastebin.com/raw/{pastebincode}").text
    api.edit(pastebincode, old + "\n" + hwid)
    embed = discord.Embed(title="Success",
                          description=f"Add Hwid : {hwid}",
                          color=0x00ff00,
                          timestamp=datetime.utcnow())
    embed.set_thumbnail(url="https://i.pinimg.com/originals/70/a5/52/70a552e8e955049c8587b2d7606cd6a6.gif")
    embed.set_footer(text="NDEZ")
    await ctx.send(embed=embed)



@bot.command()
@has_permissions(administrator=True)
async def removehwid(ctx, hwidd):
    await ctx.message.delete()
    old = requests.get(f"https://pastebin.com/raw/{pastebincode}").text
    api.edit(pastebincode, old.replace(hwidd + "\n", ""))
    embed2 = discord.Embed(title="Success",
                           description=f"delete Hwid : {hwidd}",
                           color=0x00ff00,
                           timestamp=datetime.utcnow())
    embed2.set_thumbnail(url="https://i.pinimg.com/originals/70/a5/52/70a552e8e955049c8587b2d7606cd6a6.gif")
    embed2.set_footer(text="NDEZ")
    await ctx.send(embed=embed2)


bot.run(token)
