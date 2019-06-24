import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server')

@client.command()
async def kick(ctx,member:discord.Member,*,reason=None):
    await member.kick(reason = reason)
    print(f'kicked {member} from {ctx.Message.guild}')
@client.command()
async def kick(ctx,member:discord.Member,*,reason=None):
    await member.ban(reason = reason)
    print(f'banned {member} from {ctx.Message.guild}')
client.run(os.environ.get('MODSAREGAY'))
