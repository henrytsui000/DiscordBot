from discord.ext import commands
import discord
from core.classes import Cog_extension

import requests
from bs4 import BeautifulSoup
import urllib.parse
import json
import time
import discord
import json
from discord.ext import commands
import random
import os
from dotenv import load_dotenv

adj = ["芳香四溢", "香飄十里", "油而不膩", "香脆可口", "鹹甜適中", "甘脆爽口", "五味俱全", "酸甜可口", "鮮美多汁", "清爽可口", "質嫩爽口", "麻辣鮮香", "香甜軟糯", "香甜軟糯", "珍饈美味", "饕餮大餐"]
idx = []

class Random(Cog_extension): 
    @commands.command()
    async def nearby(self, ctx):
        for i in range(6):
            idx.append(random.randint(0, len(adj)-1))
        await ctx.send('請輸入你的郵遞區號(3個數字)')
        zip_code = await self.bot.wait_for('message', check=lambda x: x.author.id == ctx.author.id)
        print(zip_code)
        r = requests.get('https://api.opencube.tw/twzipcode?zip_code=' + zip_code.content)
        r_json = json.loads(r.text)
        # print(r_json)
        lat = r_json['data'][0]['lat']
        lng = r_json['data'][0]['lng']
        # print(lat)
        # print(lng)

        # lat, lng = get_latitude_longtitude(address)

        url = 'https://disco.deliveryhero.io/listing/api/v1/pandora/vendors'
        query = {
            'longitude': lng,  # 經度
            'latitude': lat,  # 緯度
            'language_id': 6,
            'include': 'characteristics',
            'dynamic_pricing': 0,
            'configuration': 'Variant1',
            'country': 'tw',
            'budgets': '',
            'cuisine': '',
            'sort': '',
            'food_characteristic': '',
            'use_free_delivery_label': False,
            'vertical': 'restaurants',
            'limit': 48,
            'offset': 0,
            'customer_type': 'regular'
        }
        headers = {
            'x-disco-client-id': 'web',
        }
        r = requests.get(url=url, params=query, headers=headers)
        # if r.status_code == requests.codes.ok:
        #     data = r.json()
        #     restaurants = data['data']['items']
        #     bound = random.randint(0, len(restaurants)-5)
        #     for restaurant in restaurants[bound:bound+5]:
        #         await ctx.send(restaurant['name'])
        if r.status_code == requests.codes.ok:
            data = r.json()
            restaurants = data['data']['items']
            bound = random.randint(0, len(restaurants)-6)
            rand_rest = restaurants[bound:bound+6]
            embed=discord.Embed(title="天才料理少年の推薦餐廳", description="使用random.randint打造獨一無二的體驗\n在AMD，我們追求卓越", color=0x1ee66b)
            embed.set_author(name="天才料理少年", icon_url="http://p9.pstatp.com/large/401900020bd2eaccc8fb")
            embed.set_thumbnail(url="https://cdn.oc2s.co/wp-content/uploads/2020/10/14153717/8adb5c3e1771c34af133b6e95d45eb05_75.jpg")
            embed.add_field(name=rand_rest[0]['name'], value=adj[idx[0]], inline=True)
            embed.add_field(name=rand_rest[1]['name'], value=adj[idx[1]], inline=True)
            embed.add_field(name=rand_rest[2]['name'], value=adj[idx[2]], inline=True)
            embed.add_field(name=rand_rest[3]['name'], value=adj[idx[3]], inline=True)
            embed.add_field(name=rand_rest[4]['name'], value=adj[idx[4]], inline=True)
            embed.add_field(name=rand_rest[5]['name'], value=adj[idx[5]], inline=True)
            await ctx.send(embed=embed)
        else:
            await ctx.send('請求失敗')

        @commands.command()
        async def random_food(self, ctx):
            
            with open('all_food.json') as food:
                all_food = json.load(food)
            choice = random.randint(0, len(all_food)-1)
            # await ctx.send(choice)
            # await ctx.send(all_food[choice])
            cfood = all_food[choice]
            # await ctx.send(choice)
            embed=discord.Embed(title="這是一個發生在天才小時候的故事......", description='''睡前，我替陛下說了一個故事。 故事中運用了一句成語，萬中選一。 「什麼是萬中選一？」陛下睜開眼好奇問。 「就是⋯⋯你在一萬個東西中，只選了那一個。」我努力解釋。「所以那一個一定是最好的、最特別的，你最喜歡的。」 陛下點點頭。''' , color=0xeeff00)
            embed.set_author(name='天才料理少年', icon_url='http://p9.pstatp.com/large/401900020bd2eaccc8fb')
            embed.set_thumbnail(url='https://cdn.oc2s.co/wp-content/uploads/2020/10/14153717/8adb5c3e1771c34af133b6e95d45eb05_75.jpg')
            embed.add_field(name=f"「{cfood}，小當家推薦你吃萬中選一的{cfood}。」", value=f' \\ {cfood} {cfood} {cfood} / ', inline=False)
            await ctx.send(embed=embed)    
            
    @commands.command()
    async def random_food(self, ctx):
        with open('all_food.json') as food:
            all_food = json.load(food)
        choice = random.randint(0, len(all_food)-1)
        # await ctx.send(choice)
        # await ctx.send(all_food[choice])
        cfood = all_food[choice]
        # await ctx.send(choice)
        embed=discord.Embed(title="這是一個發生在天才小時候的故事......", description='''睡前，我替陛下說了一個故事。 故事中運用了一句成語，萬中選一。 「什麼是萬中選一？」陛下睜開眼好奇問。 「就是⋯⋯你在一萬個東西中，只選了那一個。」我努力解釋。「所以那一個一定是最好的、最特別的，你最喜歡的。」 陛下點點頭。''' , color=0xeeff00)
        embed.set_author(name='天才料理少年', icon_url='http://p9.pstatp.com/large/401900020bd2eaccc8fb')
        embed.set_thumbnail(url='https://cdn.oc2s.co/wp-content/uploads/2020/10/14153717/8adb5c3e1771c34af133b6e95d45eb05_75.jpg')
        embed.add_field(name=f"「{cfood}，小當家推薦你吃萬中選一的{cfood}。」", value=f' \\ {cfood} {cfood} {cfood} / ', inline=False)
        await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(Random(bot))