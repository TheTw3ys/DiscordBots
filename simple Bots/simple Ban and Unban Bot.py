import discord
from discord.ext import commands
from discord.ext.commands import command
from discord import Member

bot = commands.Bot(command_prefix=",")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason = None):
    await member.ban(reason=reason)
    await ctx.send("Banned {member.mention} for {reason}")

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

bot.run("")