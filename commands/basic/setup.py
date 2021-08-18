from discord.ext import commands
import discord
from core.classes import Cog_extension
#import message

bot = discord.Client()

string = "!mother for call u to eat\n!BLABLABLA\n" 

class Setup(Cog_extension):

    @commands.command()
    async def help(self, ctx):
        await ctx.send(string)

def setup(bot):
    bot.add_cog(Setup(bot))