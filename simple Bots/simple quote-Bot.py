import discord
from discord.ext import commands
from discord.ext.commands import command
from discord.ext.commands.help import HelpCommand
import requests 
import json

bot = commands.Bot(command_prefix=",")

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@bot.event
async def on_ready():
    print("We have logged in as {bot.user}")

@bot.command()
async def quote(ctx):
    quote = get_quote()
    await ctx.send(quote)

bot.run('TOKEN')