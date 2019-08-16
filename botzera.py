import discord
from discord.ext import commands
from discord import voice_client

TOKEN = ''
client = commands.Bot('-')

@client.event
async def on_ready():
    print('Pronto para ação!')

@client.command()
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

