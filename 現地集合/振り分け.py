# -*- coding: utf-8 -*-

from discord.ext import commands
import discord
import os
import traceback
import random


bot = commands.Bot(command_prefix='/',help_command=None)
token = 'NzI5NjMxMDM5ODI3NDc2NTUx.XwL39g.1WQPnKUAbkA4VatPYiU2xqhZlxc'




#エラーを出した時の処理
@bot.event
async def on_command_error(ctx, error):
    manage_guild = bot.get_guild(729633211025457222)
    error_ch = manage_guild.get_channel(729633338792607745)
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    error_embed = discord.Embed(title='エラーが発生しました',description=str(ctx.guild.id),color=discord.Colour.red())
    error_embed.add_field(name='Traceback',value='```'+error_msg+'```',inline=False)
    await error_ch.send(embed=error_embed)


#ぼっとが準備かんりょーした時の処理だけどいらないので破棄
@bot.command()
async def reload(ctx,name):
    bot.reload_extension(str(name))
    await ctx.send('reload code')

@bot.command()
async def rule(ctx):
    f = open(r'C:\Users\hyugo\Desktop\現地集合\rule.txt',encoding='utf-8')
    data = f.read()
    f.close()
    await ctx.send(data)

@bot.command()
async def role(ctx):
    f = open(r'C:\Users\hyugo\Desktop\現地集合\invite.txt',encoding='utf-8')
    data = f.read()
    f.close()
    await ctx.send(data)

@bot.command()
async def record(ctx):
    f = open(r'C:\Users\hyugo\Desktop\現地集合\record.txt',encoding='utf-8')
    data = f.read()
    f.close()
    await ctx.send(data)
    

@bot.event
async def on_ready():
    print('ready')


@bot.command()
async def omikuji(ctx):
    v = ['凶','吉','中吉','大吉']
    selecet = random.choice(v)
    await ctx.send('今日の運勢は'+selecet+'でしょう！')

bot.run(token)