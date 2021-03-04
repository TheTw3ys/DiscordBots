import discord
from discord.ext import commands
from discord.ext.commands import command
bot = commands.Bot(command_prefix= ",")

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.event
async def on_message(message): #if a user sends a message
    if message.author.bot: #checks if the author is a bot to prevent loops
        return
    else:
        if message.content.startswith("Hello"): #if the message starts with "Hello"
            await message.channel.send(f"Hello {message.author.mention}") #send message "Hello" and mention the user


@bot.run("")
