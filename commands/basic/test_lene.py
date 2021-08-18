import discord
from discord.ext import commands
import time
import os
from dotenv import load_dotenv
import reward
import poetry

import json
import asyncio
bot = commands.Bot(command_prefix='!')

@bot.command()
async def receipt(ctx, *arg):
    receipt_data=list(arg)
    receipt_data=str(receipt_data)
    receipt_data=receipt_data.split( )
    m=reward.reward_receipt(receipt_data[0][2],receipt_data[1][1:9])
    if m==0:
        await ctx.send("下次會更好！")
    else:
        await ctx.send(f'恭喜中獎！金額{m}元')

@bot.command()
async def random_poetry(ctx):
    await ctx.send(poetry.find_poetry())
    await ctx.send(" \n所以你想好要吃三小了沒？")
    '''with open("database1.json",mode='r',encoding='utf-8') as file:
        data=json.load(file)
    await ctx.send(data)'''

@bot.command()
async def what_did_i_eat(ctx):
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
    user = str(ctx.author)
    initialize_database.ini(user)
    with open("database1.json",mode='r',encoding='utf-8') as file:
        data=json.load(file,strict=False)

    outp="你吃了"
    for item in range(len(data["people"])):
        flag=0
        if user in data["people"][item]:
            for i in data["people"][item][user][0]["evereat"]:
                if flag!=0:
                    outp+="、"
                flag=1
                outp+=i

    await ctx.send(outp)
    await ctx.send("怎麼沒有試試看香菜皮蛋豬血糕披薩呢？")

@bot.command()
async def set_alarm(ctx,*arg):
    alarm=str(arg)
    user=(str(ctx.author))
    initialize_database.ini(user)
    with open("database1.json",mode='r',encoding='utf-8') as file:
        data=json.load(file,strict=False)
    for item in range(len(data["people"])):
        if user in data["people"][item]:
            data["people"][item][user][5]["alarm_clock"].append(alarm[2:4]+":"+alarm[5:7])
    #await ctx.send(data)
    with open("database1.json",mode="w",encoding='utf-8') as file:
            json.dump(data,file)
    await ctx.send("設定鬧鐘成功！")

stop_alarm_flag=0
'''@bot.command()
async def stop_alarm(ctx,*arg):
    stop_alarm_flag=1'''

@bot.command()
async def use_alarm(ctx,*arg):
    stop_alarm_flag=0
    alarm=str(arg)
    user=(str(ctx.author))
    initialize_database.ini(user)
    with open("database1.json",mode='r',encoding='utf-8') as file:
        data=json.load(file,strict=False)
    for item in range(len(data["people"])):
        if user in data["people"][item]:
            if len(data["people"][item][user][5]["alarm_clock"])==0:
                await ctx.send("您沒有鬧鐘")
                break
            await ctx.send("開始使用鬧鐘！")
            while(1):
                flag=0
                for alarm_time in data["people"][item][user][5]["alarm_clock"]:
                    t=time.localtime(time.time())
                    if alarm_time[0:2]==str(t.tm_hour) and alarm_time[3:5]==str(t.tm_min):
                        await ctx.send(f'<@{ctx.message.author.id}>鬧鐘響了')
                        await asyncio.sleep(30)
                        flag=1
                await ctx.send(stop_alarm_flag)
                '''if stop_alarm_flag==1:
                    await ctx.send("停止鬧鐘")
                    return'''
                if flag==0:
                       await asyncio.sleep(30)


@bot.command()
async def what_alarm_do_i_have(ctx):
    user=str(ctx.author)
    initialize_database.ini(user)
    with open("database1.json",mode='r',encoding='utf-8') as file:
        data=json.load(file,strict=False)
    a="您的鬧鐘有："
    for item in range(len(data["people"])):
        if user in data["people"][item]:
            flag=0
            for alarm_time in data["people"][item][user][5]["alarm_clock"]:
                if flag==1:
                    a+="、"
                flag=1
                a+=alarm_time
    await ctx.send(a)

@bot.command()
async def del_alarm(ctx,*arg):
    alarm=str(arg)
    alarm=alarm[2:7]
    user=(str(ctx.author))
    initialize_database.ini(user)
    with open("database1.json",mode='r',encoding='utf-8') as file:
        data=json.load(file,strict=False)
    for item in range(len(data["people"])):
        if user in data["people"][item]:
            flag=0
            for i in data["people"][item][user][5]["alarm_clock"]:
                #await ctx.send(alarm)
                #await ctx.send(i)
                if i==alarm:
                    data["people"][item][user][5]["alarm_clock"].remove(i)
                    await ctx.send("刪除成功")
                    flag=1
            if flag==0:
                await ctx.send("您沒有此鬧鐘")
    with open("database1.json",mode="w",encoding='utf-8') as file:
        json.dump(data,file)
    
    
                    






load_dotenv()
bot.run(os.getenv("TOKEN"))
