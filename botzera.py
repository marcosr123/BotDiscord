import discord
import random
from discord.ext import commands
from discord import voice_client

TOKEN = 'NjExOTA0ODMxMjc1MjcwMTQ4.XVam0A.Xnwu8JhFFhO9s1YF5vgnE377GWE'
client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('clientes no ar!'))
    print('Pronto para ação!')

@client.event
async def on_member_join(member):
    print(f'O(a) {member} se juntou ao bando!')
'''
@client.command()
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
'''

@client.command(aliases=['8ball','ball'])
async def _8ball(ctx, *, question):
    respostas = ['É certo',
        'É decididamente assim',
        'Sem dúvida',
        'Sim - definitivamente',
        'Você pode confiar nisso',
        'Como eu vejo, sim',
        'Bem provável',
        'Me parece bom',
        'Sim',
        'Sinais apontam para sim.',
        'Resposta nebulosa, tente novamente.',
        'Pergunte novamente mais tarde.',
        'Melhor não te contar agora.',
        'Não é possível prever agora.',
        'Concentre-se e pergunte novamente.',
        'Não conte com isso.',
        'Minha resposta é não.',
        'Minhas fontes dizem que não.',
        'Muito duvidoso.',
        'Me pareceu que não é bom.']
    await ctx.send(f'Pergunta: {question}\nResposta: {random.choice(respostas)}')

@client.command()
async def clear(ctx, amount=3):
    await ctx.channel.purge(limit=amount)

client.run(TOKEN)

