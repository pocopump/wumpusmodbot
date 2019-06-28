import discord
from discord.ext import commands,tasks
import os
import random
import asyncio
from discord.ext.commands import Bot

bad_words = ['nigga','bitch','whore','twat','fuck','shit','nigger']
client = Bot(command_prefix = '?', case_insensitive = True)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(status = discord.Status.online, activity=discord.Game('i literally live in powershell'))

@client.event
async def on_member_join(member):
    channel = client.get_channel(592853778538037248)
    await channel.send(f'{member} has joined the server ')
    print(f'{member} has joined a server')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server')

@client.command()
@commands.has_role("moderator")
async def kick(ctx,member:discord.Member,*,reason=None):
    await member.kick(reason = reason)
    print(f'kicked {member} from {ctx.Message.guild}')

@client.command()
@commands.has_role("moderator")
async def ban(ctx,member:discord.Member,*,reason=None):
    await member.ban(reason = reason)
    print(f'banned {member} from {ctx.message.guild}')

@client.command()
async def clear(ctx,amount:int):
    await ctx.channel.purge(limit = amount)
    print(f'cleared {amount} message(s)')
'''
@client.event
async def on_command_error(ctx,error):
    pass
'''
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('specify an amound of messages to delete')


@client.event
async def on_message(message):
    for bad_word in bad_words:
        if bad_word in message.content.strip().lower():
            await message.channel.send("{}, your message has been censored.".format(message.author.mention))
            await message.delete()

'''
@client.command()
@commands.has_role("moderator")
async def vote():
'''

client.run(os.environ.get('MODSAREGAY'))
