import discord
from discord.ext import commands

class messager(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_guild_join(self,guild):
        ch_li = guild.channels
        for ch in ch_li:
            ch_name = ch.name
            if ch.name == 'クリップ提出':
                f = open(r'C:\Users\hyugo\Desktop\現地集合\record.txt',encoding='utf-8')
                data = f.read()
                f.close()
                await ch.send(data)
            elif ch.name == 'ルール':
                f = open(r'C:\Users\hyugo\Desktop\現地集合\rule.txt',encoding='utf-8')
                data = f.read()
                f.close()
                await ch.send(data)
            elif ch.name == 'id確認':
                f = open(r'C:\Users\hyugo\Desktop\現地集合\role.txt',encoding='utf-8')
                data = f.read()
                f.close()
                await ch.send(data)
            else:
                pass
            
    @commands.Cog.listener()
    async def on_member_join(self,member):
        embed = discord.Embed(title='現地集合サーバーへようこそ！',description=member.display_name,color=discord.Colour.orange())
        embed.add_field(name='やっていただきたいこと①',value='ルールのチャンネルの確認をお願いいたします。',inline=False)
        embed.add_field(name='やっていただきたいこと②',value='idのチャンネルの確認をお願いいたします。',inline=False)
        embed.add_field(name='やっていただきたいこと③',value='クリップ提出のチャンネルの確認をお願いいたします。',inline=False)
        if member.guild.system_channel == None:
            pass
        else:
            await member.guild.system_channel.send(embed=embed)
            
            
def setup(bot):
    bot.add_Cog(messager(bot))
    
               
            
        
