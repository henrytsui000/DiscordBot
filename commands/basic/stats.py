import discord
from discord.ext import commands
import os
import json
import commands.database.initialize_database as idd
from dotenv import load_dotenv

import sys
sys.path.insert(1, '/root/hackathonv2/')
from core.classes import Cog_extension

# {"people": [{"ivy": [{"evereat": []}, {"ranking": 0}, {"money": 0}, {"vegvolume": 0}, {"veg": 0}]}]}
class stats(Cog_extension):
    def __init__(self, bot):
        with open("./database1.json",mode='r',encoding='utf-8') as file:
            self.data=json.load(file,strict=False)

    @commands.command()
    async def what_did_i_eat(self, ctx):
        user = str(ctx.author)
        '''
        name=str(ctx.author)
        initialize_database.ini(name)
        with open("database.json",mode='r',encoding='utf-8') as file:
            data=json.load(file,strict=False)
        #await ctx.send(name)
        for item in range(len(data["people"])):
            if name in data["people"][item]:
                await ctx.send(data["people"][item][name][0]["evereat"])
                for food in data["people"][item][name][0]["evereat"]:
                    await ctx.send(food)
                return
        '''

        with open("../../database1.json",mode="w",encoding='utf-8') as file:
            json.dump(self.data,file)
        outp="你吃了"
        for item in range(len(self.data["people"])):
            flag=0
            if user in self.data["people"][item]:
                for i in self.data["people"][item][user][0]["evereat"]:
                    if flag!=0:
                        outp+="、"
                    flag=1
                    outp+=i

        await ctx.send(outp)
        await ctx.send("怎麼沒有試試看香菜皮蛋豬血糕披薩呢？")

    @commands.command()
    async def ate(self, ctx, *, args):
        user = str(ctx.author)
        idd.ini(user)
        id = 0
        for item in range(len(self.data["people"])):
            if user in self.data["people"][item]:
                id = item
                break
        self.data["people"][id][user][0]["evereat"].append(args)
        with open("../../database1.json",mode="w",encoding='utf-8') as file:
            json.dump(self.data,file)
        out = "你吃了:\n"
        dic = {}
        for i in self.data["people"][id][user][0]["evereat"]:
            dic[i] = 1
        for i in dic:
            out += i
            out += ' '
        await ctx.send(out)

    @commands.command()
    async def addmoney(self, ctx,* ,args):
        user = str(ctx.author)
        idd.ini(user)
        x = int(args)
        id = 0
        for item in range(len(self.data["people"])):
            if user in self.data["people"][item]:
                id = item
                break

        self.data["people"][id][user][2]["money"] += x
        cost = self.data["people"][id][user][2]["money"]
        with open("../../database1.json",mode="w",encoding='utf-8') as file:
            json.dump(self.data,file)
        await ctx.send(f"你在食物上面已經花了: ${cost}, 吃貨")

        
    @commands.command()
    async def addvegetable(self, ctx, *, args):
        user = str(ctx.author)
        idd.ini(user)
        x = int(args)
        id = user
        for item in range(len(self.data["people"])):
            if user in self.data["people"][item]:
                id = item
                break

        self.data["people"][id][user][3]["vegvolume"] += 100*x
        vol = self.data["people"][id][user][3]["vegvolume"]
        with open("../../database1.json",mode="w",encoding='utf-8') as file:
            json.dump(self.data,file)
        await ctx.send(f"你總共吃了{vol}g蔬菜!")

    @commands.command()
    async def farm(self, ctx):
        user = str(ctx.author)
        idd.ini(user)
        id = user
        for item in range(len(self.data["people"])):
            if user in self.data["people"][item]:
                id = item
                break
        num = self.data["people"][id][user][3]["vegvolume"]
        num = num//300
        if(num == 0):
            await ctx.send("多吃菜!你沒有農場!")
        elif(num == 1):
            await ctx.send("這是你的蔬菜農場!",file=discord.File('./src/star/0.jpg'))
        elif(num == 2):
            await ctx.send("這是你的蔬菜農場!",file=discord.File('./src/star/1.jpg'))
        elif(num == 3): 
            await ctx.send("這是你的蔬菜農場!",file=discord.File('./src/star/2.jpg'))
        elif(num == 4):
            await ctx.send("這是你的蔬菜農場!",file=discord.File('./src/star/3.jpg'))
        elif(num == 5):
            await ctx.send("這是你的蔬菜農場!",file=discord.File('./src/star/4.jpg'))
        elif(num == 6):
            await ctx.send("這是你的蔬菜農場!",file=discord.File('./src/star/5.jpg'))
        else:
            await ctx.send("這是你的蔬菜農場!",file=discord.File('./src/star/6.jpg'))
            await ctx.send("做得好!重新開始計算!")
            self.data["people"][id][user][3]["vegvolume"] = 0
        with open("../../database1.json",mode="w",encoding='utf-8') as file:
            json.dump(self.data,file)

def setup(bot):
    bot.add_cog(stats(bot))