import discord
from discord.ext import commands
from discord.ext.commands import command

bot = commands.Bot(command_prefix = ",")

@bot.event
async def on_ready():
    print("We have logged in as {bot.user}")

@bot.comamnd(name="ping", aliases= ["latency"])
async def ping(ctx):
   await ctx.send(f"Pong! {round(bot.latency * 1000)} ms") 

bot.run("")