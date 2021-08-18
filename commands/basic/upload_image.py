from discord.ext import commands
import discord
from core.classes import Cog_extension

class upload(Cog_extension):
    #@commands.Cog.listener()
    #async def on_message(self,message): 
    #    if message.attachments and message.author != self.bot:
    #        await message.channel.send("讚!繼續上傳食物照片喔! (不要唬我我很笨")
    @commands.command()
    async def upload(self, ctx):
        await ctx.send("請上傳你吃的食物的照片")
        msg = await self.bot.wait_for("message", check=lambda x: x.author == ctx.author)
        if msg.attachments:
            await ctx.send("讚!繼續上傳食物照片喔! (不要唬我我很笨")
            return

def setup(bot):
    bot.add_cog(upload(bot))