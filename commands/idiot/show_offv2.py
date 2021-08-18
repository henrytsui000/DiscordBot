from discord.ext import commands
import discord
from core.classes import Cog_extension

import asyncio

class show_off(Cog_extension):
    
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def show_off(self, ctx, name):
        await ctx.send(f'@everyone <@{ctx.message.author.id}>吃了' + name)
        guild = ctx.guild
        roles = (ctx.author.roles)
        if len(roles) >= 1:
            global reac_msg
            reac_msg = await ctx.send(f"請選擇：新增我在吃{name}的身分組1️⃣  不要新增身分組2️⃣")
            await reac_msg.add_reaction("1️⃣")
            await reac_msg.add_reaction("2️⃣")
            def check(reaction, user):
                return user == ctx.message.author and str(reaction.emoji) in ['1️⃣', '2️⃣']
            reaction, user = await self.bot.wait_for('reaction_add', timeout=10, check=check)
            if reaction.emoji == "1️⃣":
                await guild.create_role(name=f'我正在吃{name}')
                member = ctx.message.author
                role = discord.utils.get(member.guild.roles, name=f'我正在吃{name}')
                await member.add_roles(role)
            elif reaction.emoji == "2️⃣":
                await ctx.send("你是個低調的人")
            
        else:
            await guild.create_role(name=f'我正在吃{name}')
            # await ctx.send(f'Role `{name}` has been created')
            member = ctx.message.author
            role = discord.utils.get(member.guild.roles, name=f'我正在吃{name}')
            await member.add_roles(role)

        channel = ctx.author.voice.channel
        vc = await channel.connect()
        #guild = ctx.guild
        print(vc)
        # <discord.voice_client.VoiceClient object at 0x7f3784627520>
        voice_client: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=guild)
        print(voice_client)
        audio_source = discord.FFmpegPCMAudio('./src/showoff.mp3', options = "-loglevel panic") 
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)
        await asyncio.sleep(5)
        await vc.disconnect()
    
    

def setup(bot):
    bot.add_cog(show_off(bot))