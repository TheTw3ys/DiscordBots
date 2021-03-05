import discord
from discord import Member
from discord.ext import commands
from discord.ext.commands import command

bot = commands.Bot(command_prefix=",")

@bot.event
async def on_ready(message):
    print(f"logged in as {bot.user}")


@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member :discord.Member, *,reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"Kicked {member.mention}\r\n Because of {reason}")

