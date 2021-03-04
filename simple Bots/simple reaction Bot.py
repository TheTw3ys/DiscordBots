import discord
from discord.ext import commands

bot = commands.bot(command_prefix= ",")

@bot.event()
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.event()
async def on_message(message):
    if message.content.startswith("Hello"):
        await message.channel.send(f"Hello {message.author.mention}")


@bot.run('TOKEN')
