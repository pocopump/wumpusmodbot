import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '.', case_insensitive = True)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    channel = client.get_channel(592853778538037248)
    await channel.send('hello')
    print(f'{member} has joined a server')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server')

@client.command()
async def kick(ctx,member:discord.Member,*,reason=None):
    await member.kick(reason = reason)
    print(f'kicked {member} from {ctx.Message.guild}')

@client.command()
async def ban(ctx,member:discord.Member,*,reason=None):
    await member.ban(reason = reason)
    print(f'banned {member} from {ctx.Message.guild}')

@client.command()
async def clear(ctx,amount:int):
    await ctx.channel.purge(limit = amount)

@client.event
async def on_command_error(ctx,error):
    pass

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('specify an amound of messages to delete')
client.run(os.environ.get('MODSAREGAY'))
