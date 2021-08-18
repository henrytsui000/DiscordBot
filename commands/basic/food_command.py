
import os
from discord.ext import commands
import discord
from core.classes import Cog_extension
import json



class pizza_bad(Cog_extension):
    @commands.command()
    async def pizza_bad(self, ctx):

        with open('/root/hackathonv2/food_tree.json', 'r') as f:
            json_data = json.load(f)
        await ctx.channel.send('中式請打1，美式請打2，韓式請打3，日式請打4，義式請打5，台式請打6')
        name_OK = await self.bot.wait_for('message', check=lambda x: x.author.id == ctx.author.id)
        choose = name_OK.content
        if choose=='1':
            await ctx.channel.send('飯請打1，麵請打2')
            name_OK = await self.bot.wait_for('message', check=lambda x: x.author.id == ctx.author.id)
            a = name_OK.content
            if a =='1':
                sen = ""
                for i in range(len(json_data['china']['rice'])):
                    sen += (f"{json_data['china']['rice'][i]} 請輸入{i+1}, ")
                tt = f"其他請輸入{1+len(json_data['china']['rice'])}"
                sen += tt
                await ctx.channel.send(sen)
                name_OK = await self.bot.wait_for('message', check=lambda x: x.author.id == ctx.author.id)
                g = int(name_OK.content)
                if g == 1+len(json_data['china']['rice']) :
                    await ctx.channel.send('請輸入你想吃的食物')
                    name_OK = await self.bot.wait_for('message', check=lambda x: x.author.id == ctx.author.id)
                    other = name_OK.content
                    json_data['china']['rice'].append(other)
                    with open('food_tree.json','w') as fan:
                        json.dump(json_data,fan)
                    await ctx.channel.send(other)
                else :

                    await ctx.channel.send(json_data['china']['rice'][g-1])





            elif a =='2':
                pp = ""
                for i in range(len(json_data['china']['noodle'])):
                    pp += (f"{json_data['china']['noodle'][i]} 請輸入{i+1}， ")
                tt = f"其他請輸入{1+len(json_data['china']['noodle'])}"
                pp += tt
                await ctx.channel.send(sen)
                name_OK = await self.bot.wait_for('message', check=lambda x: x.author.id == ctx.author.id)
                h = int(name_OK.content)
                if h == 1+len(json_data['china']['noodle']) :
                    await ctx.channel.send('請輸入你想吃的食物')
                    name_OK = await self.bot.wait_for('message', check=lambda x: x.author.id == ctx.author.id)
                    other = name_OK.content
                    json_data['china']['noodle'].append(other)
                    with open('food_tree.json','w') as fan:
                        json.dump(json_data,fan)
                    await ctx.channel.send(other)
                else :

                    await ctx.channel.semd(json_data['china']['noodle'][h-1])


        if choose=='2':
            sen = ""
            for i in range(len(json_data['usa'])):
                sen += (f"{json_data['usa'][i]} 請輸入{i+1}, ")
            tt = f"其他請輸入{1+len(json_data['usa'])}"
            sen += tt
            await ctx.channel.send(sen)
            name_OK = await self.bot.wait_for('message', check=lambda x: x.author.id == ctx.author.id)
            i = name_OK.content
            i = int(name_OK.content)
            if i == 1+len(json_data['usa']) :
                await ctx.channel.send('請輸入你想吃的食物')
                name_OK = await self.bot.wait_for('message', check=lambda x: x.author.id == ctx.author.id)
                other = name_OK.content
                json_data['usa'].append(other)
                with open('food_tree.json','w') as fan:
                    json.dump(json_data,fan)
                await ctx.channel.send(other)
            else :

                await ctx.channel.send(json_data['usa'][i-1])

        if choose=='3':
            sen = ""
            for i in range(len(json_data['korea'])):
                sen += (f"{json_data['korea'][i]} 請輸入{i+1}, ")
            tt = f"其他請輸入{1+len(json_data['korea'])}"
            sen += tt
            await ctx.channel.send(sen)
            name_OK = await self.bot.wait_for('message', check=lambda x: x.author.id == ctx.author.id)
            j = int(name_OK.content)
            if j == 1+len(json_data['korea']) :
                await ctx.channel.send('請輸入你想吃的食物')
                name_OK = await self.bot.wait_for('message', check=lambda x: x.author.id == ctx.author.id)
                other = name_OK.content
                json_data['korea'].append(other)
                with open('food_tree.json','w') as fan:
                    json.dump(json_data,fan)
                await ctx.channel.send(other)
            else :

                await ctx.channel.send(json_data['korea'][j-1])

        if choose=='4':
            await ctx.channel.send('飯請打1，麵請打2，bbq請打3，新增其他請打4')
            name_OK = await self.bot.wait_for('message', check=lambda x: x.author.id == ctx.author.id)
            b = name_OK.content
            if b =='1':
                sen = ""
                for i in range(len(json_data['japan']['rice'])):
                    sen += (f"{json_data['japan']['rice'][i]} 請輸入{i+1}, ")
                tt = f"其他請輸入{1+len(json_data['japan']['rice'])}"
                sen += tt
                await ctx.channel.send(sen)
                name_OK = await self.bot.wait_for('message', check=lambda x: x.author.id == ctx.author.id)
                k = int(name_OK.content)
                if  k== 1+len(json_data['japan']['rice']) :
                    await ctx.channel.send('請輸入你想吃的食物')
                    name_OK = await self.bot.wait_for('message', check=lambda x: x.author.id == ctx.author.id)
                    other = name_OK.content
                    json_data['japan']['rice'].append(other)
                    with open('food_tree.json','w') as fan:
                        json.dump(json_data,fan)
                    await ctx.channel.send(other)
                else :

                    await ctx.channel.send(json_data['japan']['rice'][k-1])

            elif b =='2':
                sen = ""
                for i in range(len(json_data['japan']['noodle'])):
                    sen += (f"{json_data['japan']['noodle'][i]} 請輸入{i+1}, ")
                tt = f"其他請輸入{1+len(json_data['japan']['noodle'])}"
                sen += tt
                await ctx.channel.send(sen)
                name_OK = await self.bot.wait_for('message', check=lambda x: x.author.id == ctx.author.id)
                l = int(name_OK.content)
                if  l== 1+len(json_data['japan']['noodle']) :
                    await ctx.channel.send('請輸入你想吃的食物')
                    name_OK = await self.bot.wait_for('message', check=lambda x: x.author.id == ctx.author.id)
                    other = name_OK.content
                    json_data['japan']['noodle'].append(other)
                    with open('food_tree.json','w') as fan:
                        json.dump(json_data,fan)
                    await ctx.channel.send(other)
                else :

                    await ctx.channel.send(json_data['japan']['noodle'][l-1])
            elif b =='3':
                sen = ""
                for i in range(len(json_data['japan']['bbq'])):
                    sen += (f"{json_data['japan']['bbq'][i]} 請輸入{i+1}, ")
                tt = f"其他請輸入{1+len(json_data['japan']['bbq'])}"
                sen += tt
                await ctx.channel.send(sen)
                name_OK = await self.bot.wait_for('message', check=lambda x: x.author.id == ctx.author.id)
                m = int(name_OK.content)
                if  m== 1+len(json_data['japan']['bbq']) :
                    await ctx.channel.send('請輸入你想吃的食物')
                    name_OK = await self.bot.wait_for('message', check=lambda x: x.author.id == ctx.author.id)
                    other = name_OK.content
                    json_data['japan']['bbq'].append(other)
                    with open('food_tree.json','w') as fan:
                        json.dump(json_data,fan)
                    await ctx.channel.send(other)
                else :

                    await ctx.channel.send(json_data['japan']['bbq'][m-1])

        if choose=='5':
            sen = ""
            for i in range(len(json_data['italy'])):
                sen += (f"{json_data['italy'][i]} 請輸入{i+1}, ")
            tt = f"其他請輸入{1+len(json_data['italy'])}"
            sen += tt
            await ctx.channel.send(sen)
            name_OK = await self.bot.wait_for('message', check=lambda x: x.author.id == ctx.author.id)
            n = int(name_OK.content)
            if n == 1+len(json_data['italy']) :
                await ctx.channel.send('請輸入你想吃的食物')
                name_OK = await self.bot.wait_for('message', check=lambda x: x.author.id == ctx.author.id)
                other = name_OK.content
                json_data['italy'].append(other)
                with open('food_tree.json','w') as fan:
                    json.dump(json_data,fan)
                await ctx.channel.send(other)
            else :

                await ctx.channel.send(json_data['italy'][n-1])

        if choose=='6':
            await ctx.channel.send('小吃請打1，主食請打2')
            name_OK = await self.bot.wait_for('message', check=lambda x: x.author.id == ctx.author.id)
            c = name_OK.content
            if c =='1':
                sen = ""
                for i in range(len(json_data['taiwan']['小吃'])):
                    sen += (f"{json_data['taiwan']['小吃'][i]} 請輸入{i+1}, ")
                tt = f"其他請輸入{1+len(json_data['taiwan']['小吃'])}"
                sen += tt
                await ctx.channel.send(sen)
                name_OK = await self.bot.wait_for('message', check=lambda x: x.author.id == ctx.author.id)
                o = int(name_OK.content)
                if  o== 1+len(json_data['taiwan']['小吃']) :
                    await ctx.channel.send('請輸入你想吃的食物')
                    name_OK = await self.bot.wait_for('message', check=lambda x: x.author.id == ctx.author.id)
                    other = name_OK.content
                    json_data['taiwan']['小吃'].append(other)
                    with open('food_tree.json','w') as fan:
                        json.dump(json_data,fan)
                    await ctx.channel.send(other)
                else :

                    await ctx.channel.send(json_data['taiwan']['小吃'][o-1])
            elif c =='2':
                sen = ""
                for i in range(len(json_data['taiwan']['主食'])):
                    sen += (f"{json_data['taiwan']['主食'][i]} 請輸入{i+1}, ")
                tt = f"其他請輸入{1+len(json_data['taiwan']['主食'])}"
                sen += tt
                await ctx.channel.send(sen)
                name_OK = await self.bot.wait_for('message', check=lambda x: x.author.id == ctx.author.id)
                p = int(name_OK.content)
                if  p== 1+len(json_data['taiwan']['主食']) :
                    await ctx.channel.send('請輸入你想吃的食物')
                    name_OK = await self.bot.wait_for('message', check=lambda x: x.author.id == ctx.author.id)
                    other = name_OK.content
                    json_data['taiwan']['主食'].append(other)
                    with open('food_tree.json','w') as fan:
                        json.dump(json_data,fan)
                    await ctx.channel.send(other)
                else :

                    await ctx.channel.send(json_data['taiwan']['主食'][p-1])





def setup(bot):
    bot.add_cog(pizza_bad(bot))
