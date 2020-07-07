import discord
from discord.ext import discord


class pointcheck(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.allpt = dict()
        self.mutch = dict()
        self.kill = dict()
        self.ct = dict()
        self.member = list()
        self.guild = bot.get_guild('決勝サーバーid')
        self.counter
        
    @commands.command()
    async def registor(self,ctx):
        if ctx.channel.id == '代表者チャンネルid':
            mem =self.guild.get_member(ctx.author.id)
            name = mem.display_name
            if ctx.author.id in self.member:
                await ctx.send(name+'さんの登録は完了しています。')
            else:
                self.member.append(ctx.author.id)
                self.allpt[ctx.author.id] = 0
                self.mutch[ctx.author.id] = 0
                self.kill[ctx.author.id] = 0
                self.ct[ctx.author.id] = 0
                await ctx.send(name+'さんの参加を受け付けました')
        else:
            pass
    
    @commands.command()
    async def submit(self,ctx,k=None,rank=None):
        if ctx.channel.id == '代表者チャンネルid':
            if ctx.author.id in self.member:
                kill_pass = False
                rank_pass = False
                user = self.guild.get_member(ctx.author.id)
                username = user.display_name
                if k != None and rank != None and self.ct[ctx.author.id] <= 3:
                    if k.isdecimal() == True and rank.isdecimal() == True:
                        int_k = int(k)
                        int_rank = int(rank)
                        if int_k <= 96:
                            killpt = int_k*5
                            past_kill = self.kill[ctx.author.id]
                            self.kill[ctx.author.id] = killpt + past_kill
                            kill_pass = True
                            await ctx.send(username+'さんのキル数を記録しました。')
                        else:
                            await ctx.send('96killを超えることはできません。スタッフにリセットしてもらってから一試合目から順に正しい値を記録してください')
                        if int_rank <=33:
                            past_rank = self.mutch[ctx.author.id]
                            if int_rank >= 4:
                                self.mutch[ctx.author.id] = past_rank + (34 - int_rank)
                                rank_pass = True
                                if kill_pass == True:
                                    past_ct = self.ct[ctx.author.id]
                                    self.ct[ctx.author.id] =past_ct + 1
                                    self.allpt[ctx.author.id] = self.kill[ctx.author.id] + self.mutch[ctx.author.id]
                                await ctx.send(username+'さんの順位を記録しました。')
                            elif int_rank == 3:
                                self.mutch[ctx.author.id] = past_rank + 35
                                rank_pass = True
                                if kill_pass == True:
                                    past_ct = self.ct[ctx.author.id]
                                    self.ct[ctx.author.id] =past_ct + 1
                                    self.allpt[ctx.author.id] = self.kill[ctx.author.id] + self.mutch[ctx.author.id]
                            elif int_rank == 2:
                                self.mutch[ctx.author.id] = past_rank + 40
                                rank_pass = True
                                if kill_pass == True:
                                    past_ct = self.ct[ctx.author.id]
                                    self.ct[ctx.author.id] =past_ct + 1
                                    self.allpt[ctx.author.id] = self.kill[ctx.author.id] + self.mutch[ctx.author.id]
                            elif int_rank == 1:
                                self.mutch[ctx.author.id] = past_rank + 55
                                rank_pass = True
                                if kill_pass == True:
                                    past_ct = self.ct[ctx.author.id]
                                    self.ct[ctx.author.id] =past_ct + 1
                                    self.allpt[ctx.author.id] = self.kill[ctx.author.id] + self.mutch[ctx.author.id]
                        else:
                            await ctx.send('33位以上の順位はありません。スタッフにリセットしてもらってから一試合目から順に正しい値を記録してください')
                    else:
                        await ctx.send('kill数,順位は単位をつけずに半角数字で`/submit kill数 順位` で記録してください。')
                else:
                    await ctx.send('順位、キル数のどちらかが足りません。間に半角スペースを開けていることを確認してください。')
                
    @commands.command()
    async def check(self,ctx,args):
        if ctx.author.id == ('staffid') and args.isdecimal() == True:
            counter = int(args)
            member_n = len(self.member)
            cmp = 0
            is_pass = True
            for v in self.ct.values():
                if v == counter:
                    cmp += 1
                else:
                    is_pass = False
            if is_pass == True:
                await ctx.send('集計終わりました。')
            else:
                await ctx.send('まだ集計が終わっていません。'+str(cmp)'/'+str(member_n))
    
    @commands.command()
    async def result(self,ctx):
        ranking = sorted(self.allpt.items(), key=lambda x:x[1],reverse=True)
        c=0
        res = discord.Embed(title='結果発表',colour=discord.Colour.red())
        for member,p in rank.items():
            c = c+1
            member_g = self.bot.get_user(member)
            plyer= member_g.display_name
            res.add_field(name=str(c)'位',value=player + ':' + str(p)+'point')
        await ctx.send(embed=res)
        
    @commands.command()
    async def reset(self,ctx,args):
        if ctx.author.id == 598018755066593290:
            if args.isdecimal ==True:
                id = int(args)
                if id in self.member:
                    self.mutch[id] = 0
                    self.kill[id] = 0
                    self.allpt[id] = 0
                    self.ct[id] = 0
                    await ctx.send('リセットしました。')
        
    @commands.command()
    async def remove(self,ctx,args):
        if ctx.author.id == 598018755066593290:
            if args.isdecimal ==True:
                id = int(args)
                if id in self.member:
                    del self.mutch[id]
                    del self.kill[id]
                    del self.allpt[id]
                    del self.ct[id]
                    self.member.remove(id)
                    await ctx.send('削除しました')
                
    
    
    
    
                
                
                    
                       
                    
def setup(bot):
    bot.add_Cog(pointcheck(bot))
                                
                                
                                
      
    
                        
                        
                    
        
       
