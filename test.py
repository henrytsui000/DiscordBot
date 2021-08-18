import asyncio
from datetime import datetime, timedelta
from discord.ext import commands
import time
import sched

TOKEN = 'XXX'

client = commands.Bot(command_prefix='.')

alarm_time = '23:33'#24hrs
channel_id = '51599XXXXX5036697'

@client.event
async def on_ready():
    print('Bot Online.')


async def time_check():
    await client.wait_until_ready()
    while not client.is_closed:
        channel = client.get_channel(channel_id)
        messages = ('Test')
        f = '%H:%M'

        now = datetime.strftime(datetime.now(), f)
        diff = (datetime.strptime(alarm_time, f) - datetime.strptime(now, f)).total_seconds()

        s = sched.scheduler(time.perf_counter, time.sleep)
        args = (client.send_message(channel, message), )
        s.enter(seconds, 1, client.loop.create_task, args)


# client.loop.create_task(time_check())

client.run(TOKEN)
