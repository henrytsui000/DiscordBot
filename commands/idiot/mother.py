from discord.ext import commands
import discord
from core.classes import Cog_extension

import json
import time
import datetime
import asyncio
import os

# bot is self.bot

class mother(Cog_extension):
    @commands.command()
    async def mother(self, ctx):
        # grab the user who sent the command
        guild = ctx.guild

        channel = ctx.author.voice.channel
        vc = await channel.connect()
        print(vc)
        voice_client: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=guild)
        print(voice_client)
        audio_source = discord.FFmpegPCMAudio('./src/eat.mp3', options = "-loglevel panic")
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)
        await asyncio.sleep(5)
        await vc.disconnect()

    @commands.command()
    async def nomother(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def set_mother(self, ctx):
        await ctx.send("什麼時候要吃飯啦")
        mother_time = (await self.bot.wait_for('message', check=lambda x: x.author.id == ctx.author.id)).content
        mother_time = list(map(int, mother_time.split(":")))
        print(mother_time)

    # async def time_check():
    #     while True:
    #         f = '%H:%M'
    #         now = datetime.strftime(datetime.now(), f)
    #         alarm_time = str(mother[0] + ':' + mother_time[1])
    #         diff = (datetime.strptime(alarm_time, f) - datetime.strptime(now, f)).total_seconds()

    #         print(diff)
    #         await asyncio.sleep(1)
    #         # s = sched.scheduler(time.perf_counter, time.sleep)
    #         # args = (client.send_message(channel, message), )
    #         # s.enter(seconds, 1, client.loop.create_task, args)


def setup(bot):
    bot.add_cog(mother(bot))
