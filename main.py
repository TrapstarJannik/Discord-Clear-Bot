# discord imports
import discord
from discord.ext import commands

# other imports 
import datetime

# "bot" for commands/events, prefix ".", permissions "all"
bot = commands.Bot(command_prefix=".", intents = discord.Intents.all())

# start message 
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}") # <-- bot name
    print(f"Bot ID: {bot.user.id}") # <-- bot ID
    print("Bot is ready.") # <-- ready message
  
# clear command 
   
@bot.command(aliases=["purge", "delete"])
async def clear(ctx, amount: int = None):
    if not ctx.author.guild_permissions.manage_messages:  # <-- permissions check
        delete_embed = discord.Embed(
            title=":x: No permissions!", # <-- embed title (changeable)
            description="> You don't have the required permissions to run this command!", # <-- embed description (changeable)
            color=0xff9999) # <-- embed color (changeable)
        if ctx.author.avatar: 
            avatar_url = ctx.author.avatar.url
        else:
            avatar_url = ctx.author.default_avatar.url # <-- getting avatar for embed footer
        delete_embed.set_footer(text=f"{ctx.author.name}・{datetime.datetime.now().strftime('%I:%M:%S %p')}", icon_url=avatar_url) # <-- embed footer, time (changeable)
        await ctx.send(embed=delete_embed, delete_after=20) # <-- delete after 20s (changeable)
        return

    if amount is None:
        delete_embed = discord.Embed(
            title=":warning: Warning!",# <-- embed title (changeable)
            description=f"> You must provide a valid **number** to delete the message(s) in {ctx.channel.mention}!", # embed description (changeable)
            color=0xffffcc) # <-- embed color (changeable)
        if ctx.author.avatar:
            avatar_url = ctx.author.avatar.url
        else:
            avatar_url = ctx.author.default_avatar.url # <-- getting avatar for embed footer 
        delete_embed.set_footer(text=f"{ctx.author.name}・{datetime.datetime.now().strftime('%I:%M:%S %p')}", icon_url=avatar_url) # <-- embed footer, time (changeable)
        await ctx.send(embed=delete_embed, delete_after=20) # <-- delete after 20s
        return

    await ctx.channel.purge(limit=amount + 1) # <-- the number of deleted messages, +1
    success_embed = discord.Embed(
        title=":white_check_mark: Clear successful!", # <-- embed title (changeable)
        description=f"> Successfully deleted `{amount} message(s)` in {ctx.channel.mention}!", # <-- embed description (changeable)
        color=0xb3ffb3) # <-- embed color (changeable) 
    if ctx.author.avatar:
        avatar_url = ctx.author.avatar.url
    else:
        avatar_url = ctx.author.default_avatar.url # <-- getting avatar for embed footer
    success_embed.set_footer(text=f"{ctx.author.name}・{datetime.datetime.now().strftime('%I:%M:%S %p')}", icon_url=avatar_url) # <-- embed footer, time (changeable)
    await ctx.send(embed=success_embed, delete_after=20) # <-- delete after 20s (changeable)
    
    # Define the ID of the log channel where you want to send deletion logs.
    # Replace the placeholder below with the actual ID of your log channel.
    log_channel_id = 0000000000000  # <-- !!! PUT YOUR LOG CHANNEL ID HERE !!!
    log_channel = bot.get_channel(log_channel_id)
    if log_channel:
        log_embed = discord.Embed(title=":page_facing_up: Deleted Messages log", color=0x666699) # <-- embed title and color
        log_embed.add_field(name=":speech_balloon:・Channel", value=ctx.channel.mention) # embed field 1 (changeable)
        log_embed.add_field(name=":man_police_officer_tone3:・Moderator", value=ctx.author.mention) # embed field 2 (changeable)
        log_embed.add_field(name=":x:・Deleted Messages", value=f"`{amount}`") # embed field 3 (changeable)
        if ctx.author.avatar:
            avatar_url = ctx.author.avatar.url
        else:
            avatar_url = ctx.author.default_avatar.url # <-- getting avatar for embed footer
        log_embed.set_footer(text=f"{ctx.author.name}・{datetime.datetime.now().strftime('%I:%M:%S %p')}", icon_url=avatar_url) # <-- embed footer, time (changeable)
        await log_channel.send(embed=log_embed) # <-- send embed
    else:
        print("Log channel could not be found please check the channel ID")
        
with open("token.txt") as f:
    token = f.read()

bot.run(token)
